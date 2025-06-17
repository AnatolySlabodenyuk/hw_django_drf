# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import viewsets
from .models import Sensor
from .serializers import SensorDetailSerializer, SensorListSerializer
from .models import Measurement
from .serializers import MeasurementCreateSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SensorDetailSerializer
        elif self.action == 'list':
            return SensorListSerializer
        return SensorDetailSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer
