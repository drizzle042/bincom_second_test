from rest_framework.views import APIView
from main_app.controller.auth import AuthController
from main_app.controller.polling_unit import PollingUnitsController
from main_app.controller.polling_unit_result import PollingUnitResultController
from main_app.controller.pu_and_results_by_LGA import PollingUnitsAndResultsByLGAController
from main_app.controller.lgas import LgasController


# Create your views here.
class GenerateAuth(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = AuthController()
    
    authentication_classes = []

    def post(self, request):
        return self.controller.get_access_token_response(request)


class PollingUnits(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = PollingUnitsController()

    def get(self, request):
        return self.controller.get_polling_units_response(request)


class PollingUnitResults(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = PollingUnitResultController()

    def get(self, request):
        return self.controller.get_polling_unit_results_response(request)


class Lgas(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = LgasController()

    def get(self, request):
        return self.controller.get_lgas_response(request)


class PollingUnitsAndResultsByLGA(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = PollingUnitsAndResultsByLGAController()

    def get(self, request):
        return self.controller.get_pu_and_results_by_LGA_response(request)

    def post(self, request):
        return self.controller.create_pu_and_results_by_LGA_response(request)
