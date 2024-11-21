from pathlib import Path
import json
from typing import Dict, List, Set
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TypeGenerator:
    def __init__(self):
        self.generated_types: Set[str] = set()
        self.type_dependencies: Dict[str, Set[str]] = {}
        self.types_dir = Path(__file__).parent / "types"
        self.types_dir.mkdir(exist_ok=True)
        
    def get_python_type(self, gql_type: Dict) -> str:
        """Convert GraphQL type to Python type string"""
        kind = gql_type["kind"]
        name = gql_type.get("name")
        of_type = gql_type.get("ofType")
        
        type_mapping = {
            "String": "str",
            "Int": "int",
            "Float": "float",
            "Boolean": "bool",
            "ID": "str",
            "Long": "int",
        }
        
        if kind == "NON_NULL":
            return self.get_python_type(of_type)
        elif kind == "LIST":
            inner_type = self.get_python_type(of_type)
            return f"List[{inner_type}]"
        elif kind == "SCALAR":
            return type_mapping.get(name, "Any")
        else:
            return f"Optional[{name}]"
    
    def analyze_dependencies(self, types: List[Dict]):
        """Build dependency graph before generating any files"""
        for type_def in types:
            if type_def["kind"] not in ["OBJECT", "ENUM"]:
                continue
                
            name = type_def["name"]
            if name.startswith("__"):
                continue
                
            deps = set()
            if type_def["kind"] == "OBJECT":
                for field in type_def["fields"]:
                    field_type = self.get_python_type(field["type"])
                    deps.update(self.extract_type_names(field_type))
            
            self.type_dependencies[name] = deps
    
    def extract_type_names(self, type_str: str) -> Set[str]:
        """Extract referenced type names from a type string"""
        names = set()
        if "[" in type_str:  # List[Type] or Optional[Type]
            inner = type_str[type_str.index("[") + 1:type_str.rindex("]")]
            if inner not in ["str", "int", "float", "bool", "Any"]:
                names.add(inner.replace("Optional[", "").replace("]", ""))
        elif type_str not in ["str", "int", "float", "bool", "Any"]:
            names.add(type_str)
        return names
    
    def generate_types(self, types: List[Dict]):
        """Generate types in dependency order"""
        self.analyze_dependencies(types)
        
        # Create __init__.py
        (self.types_dir / "__init__.py").write_text(
            "from typing import TYPE_CHECKING\n\n" +
            "if TYPE_CHECKING:\n" +
            "    # Import all types for type checking\n" +
            "\n".join(f"    from .{name.lower()} import {name}" 
                     for name in self.type_dependencies.keys())
        )
        
        # Generate files
        for type_def in types:
            if type_def["kind"] in ["OBJECT", "ENUM"]:
                self.generate_type_file(type_def)
    
    def generate_type_file(self, type_def: Dict):
        name = type_def["name"]
        if name.startswith("__") or name in self.generated_types:
            return
            
        if type_def["kind"] == "OBJECT":
            content = self.generate_dataclass(type_def)
        else:  # ENUM
            content = self.generate_enum(type_def)
            
        file_path = self.types_dir / f"{name.lower()}.py"
        file_path.write_text(content)
        self.generated_types.add(name)
    
    def generate_dataclass(self, type_def: Dict) -> str:
        fields = []
        imports = {"from dataclasses import dataclass"}
        forward_refs = set()
        
        for field in type_def["fields"]:
            field_type = self.get_python_type(field["type"])
            if "Optional" in field_type:
                imports.add("from typing import Optional")
            if "List" in field_type:
                imports.add("from typing import List")
                
            # Handle circular dependencies with forward refs
            for dep in self.extract_type_names(field_type):
                if dep != type_def["name"]:  # Skip self-references
                    forward_refs.add(dep)
                    
            fields.append(f"    {field['name']}: {field_type}")
        
        # Build imports section
        import_lines = []
        
        # Regular imports first
        regular_imports = sorted(imp for imp in imports if not imp.startswith("if TYPE_CHECKING"))
        import_lines.extend(regular_imports)
        
        # Then TYPE_CHECKING block if needed
        if forward_refs:
            import_lines.append("from typing import TYPE_CHECKING")
            import_lines.append("")
            import_lines.append("if TYPE_CHECKING:")
            for ref in sorted(forward_refs):
                import_lines.append(f"    from .{ref.lower()} import {ref}")
            import_lines.append("")  # Extra newline after imports
        
        return f"""{chr(10).join(import_lines)}

@dataclass
class {type_def['name']}:
    \"\"\"
    {type_def.get('description', 'No description available.')}
    \"\"\"
{chr(10).join(fields)}
"""

    def generate_enum(self, type_def: Dict) -> str:
        """Generate Python enum class from GraphQL enum type"""
        values = []
        for value in type_def.get("enumValues", []):
            name = value["name"]
            values.append(f"    {name} = \"{name}\"")
            
        return f"""
from enum import Enum

class {type_def['name']}(Enum):
    \"\"\"
    {type_def.get('description', 'No description available.')}
    \"\"\"
{chr(10).join(values)}
"""

def generate_types_from_schema():
    schema_path = Path(__file__).parent / "schema.graphql"
    logger.info(f"Looking for schema at: {schema_path}")
    
    schema_data = json.loads(schema_path.read_text())
    types = schema_data.get("__schema", {}).get("types", [])
    
    generator = TypeGenerator()
    generator.generate_types(types)

if __name__ == "__main__":
    generate_types_from_schema()