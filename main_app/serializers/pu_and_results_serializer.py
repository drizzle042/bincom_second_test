from rest_framework.serializers import Serializer
from main_app.serializers.polling_unit_serializer import PollingUnitSerializer
from main_app.serializers.polling_unit_result_serializer import PollingUnitResultSerializer


class PUAndResultsSerializer(Serializer):
    polling_unit = PollingUnitSerializer()
    polling_unit_results = PollingUnitResultSerializer(required=False, many=True)
