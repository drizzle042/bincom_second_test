from repository.base_repo import BaseRepo
from main_app.models import AnnouncedPuResults


class PollingUnitResultsRepo(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = AnnouncedPuResults
        self.filter_fields = "result_id", "polling_unit_uniqueid", "party_abbreviation", "party_score", "entered_by_user", "date_entered"
