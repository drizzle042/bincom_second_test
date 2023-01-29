from rest_framework.serializers import ModelSerializer
from main_app.models import Lga


class LgaSerializer(ModelSerializer):
    class Meta:
        model = Lga
        exclude = ["user_ip_address"]