from typing import Iterator, Optional, List, Dict
from datetime import datetime
from ..models.base import ApiObject

class ReportsResource:
    def __init__(self, client):
        self.client = client
        self.base_path = "myreports"
    
    def get_schedule(self, schedule_id: int) -> ApiObject:
        
        endpoint = f"{self.base_path}/reportschedule/{schedule_id}"
        result = self.client.get(endpoint)
        return ApiObject(**result)

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

    def download_report(self, report_url: str) -> tuple[bytes, str]:
       
        response = self.client.session.get(
            report_url,
            headers=self.client._get_headers(),
            stream=True,
            allow_redirects=True  # Follow S3 redirects
        )
        
        return response.content, response.url

    def list_executions_by_partners(
        self,
        partner_ids: List[str],
        page_size: int = 25,
        page_start_index: int = 0,
        execution_spans_end_date: Optional[datetime] = None,
        execution_spans_start_date: Optional[datetime] = None,
        report_execution_states: Optional[List[str]] = None,
        report_schedule_ids: Optional[List[int]] = None,
        report_schedule_name_contains: Optional[str] = None,
        sort_fields: Optional[List[Dict[str, str]]] = None,
    ) -> Iterator[ApiObject]:
        
        data = {
            "PartnerIds": partner_ids,
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
            f"{self.base_path}/reportexecution/query/partners",
            data=data,
            page_size=page_size
        ):
            yield ApiObject(**result)