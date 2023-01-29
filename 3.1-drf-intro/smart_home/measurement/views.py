# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorsAPI(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorAPI(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementAPI(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer
