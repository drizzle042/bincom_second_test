from rest_framework.serializers import ModelSerializer
from main_app.models import PollingUnit


class PollingUnitSerializer(ModelSerializer):
    class Meta:
        model = PollingUnit
        exclude = ["user_ip_address"]