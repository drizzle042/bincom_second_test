from repository.base_repo import BaseRepo
from main_app.models import Lga


class LgasRepo(BaseRepo):
    def __init__(self) -> None:
        super().__init__()
        self.model = Lga
        self.filter_fields = "uniqueid", "lga_id", "lga_name", "state_id", "lga_description", "entered_by_user", "date_entered"
        