from rest_framework.serializers import ModelSerializer
from main_app.models import AnnouncedPuResults


class PollingUnitResultSerializer(ModelSerializer):
    class Meta:
        model = AnnouncedPuResults
        exclude = ["user_ip_address"]