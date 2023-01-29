from repository.base_repo import BaseRepo
from main_app.models import PollingUnit


class PollingUnitsRepo(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = PollingUnit
        self.filter_fields = "uniqueid", "polling_unit_id", "ward_id", "lga_id", "uniquewardid", "polling_unit_number", "polling_unit_name", "polling_unit_description", "lat", "long", "entered_by_user", "date_entered"
