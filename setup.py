from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ttd_sdk",
    version="0.1.0",
    author="Adam Hunter",
    author_email="ahunter@pathlabs.com",
    description="Python SDK for The Trade Desk API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hunterad93/ttd_sdk",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "requests>=2.32.3",
        "pydantic>=2.7.3",
        "python-dotenv>=1.0.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
)