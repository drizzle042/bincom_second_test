from rest_framework.authentication import BaseAuthentication
from exceptions.pythonic_exceptions import FieldRequired
from main_app.controller.auth import AuthController

class CustomAuthentication(BaseAuthentication):
    def __init__(self) -> None:
        super().__init__()
        self.auth_controller = AuthController()

    def authenticate(self, request):
        try:
            authorization = request.headers["authorization"]
        except KeyError:
            raise FieldRequired("An authorization key in header is required")
        [*_, token] = authorization.split()
        code = self.auth_controller.get_code_from_token(token).check_code()
        return code, token
        