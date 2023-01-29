from django.urls import path
from main_app import views

app_name = "main_app"

urlpatterns = [
    path("v0/main/gen-auth/", views.GenerateAuth.as_view(), name="generate_auth_tokens"),
    path("v0/main/polling-units/", views.PollingUnits.as_view(), name="polling_units"),
    path("v0/main/pu-results/", views.PollingUnitResults.as_view(), name="polling_unit_results"),
    path("v0/main/pu-and-results-by-lga/", views.PollingUnitsAndResultsByLGA.as_view(), name="polling_unit_and_results_by_lga"),
    path("v0/main/lgas/", views.Lgas.as_view(), name="lgas"),
]
