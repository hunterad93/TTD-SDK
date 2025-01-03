from typing import Iterator, Optional, List, Dict
from datetime import datetime
from ..models.base import ApiObject

class ReportsResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "myreports"
    
    def list_executions_by_advertisers(
        self,
        advertiser_ids: List[str],
        page_size: int = 25,
        page_start_index: int = 0,
        execution_spans_end_date: Optional[datetime] = None,
        execution_spans_start_date: Optional[datetime] = None,
        report_execution_states: Optional[List[str]] = None,
        report_schedule_ids: Optional[List[int]] = None,
        report_schedule_name_contains: Optional[str] = None,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[ApiObject]:
        """
        Get a paginated list of Report Executions that match the Advertisers and filters.
        
        Args:
            advertiser_ids: List of platform IDs for the advertisers
            page_size: Number of results per page (25-100 recommended)
            page_start_index: Zero-based index for pagination start
            execution_spans_end_date: Filter by report end date
            execution_spans_start_date: Filter by report start date
            report_execution_states: Filter by execution states
            report_schedule_ids: Filter by schedule IDs
            report_schedule_name_contains: Filter by schedule name
            sort_fields: Optional list of sort field configurations
        """
        data = {
            "AdvertiserIds": advertiser_ids,
            "PageSize": min(max(page_size, 25), 100),
            "PageStartIndex": page_start_index
        }

        if execution_spans_end_date:
            data["ExecutionSpansEndDate"] = execution_spans_end_date.isoformat()
        if execution_spans_start_date:
            data["ExecutionSpansStartDate"] = execution_spans_start_date.isoformat()
        if report_execution_states:
            data["ReportExecutionStates"] = report_execution_states
        if report_schedule_ids:
            data["ReportScheduleIds"] = report_schedule_ids
        if report_schedule_name_contains:
            data["ReportScheduleNameContains"] = report_schedule_name_contains
        if sort_fields:
            data["SortFields"] = sort_fields

        for result in self.client.post_with_pagination(
            f"{self.base_path}/reportexecution/query/advertisers",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)