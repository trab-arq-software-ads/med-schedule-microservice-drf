from appointments.models import Appointment
from rest_framework import viewsets
from .serializers import AppointmentProtoSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentProtoSerializer