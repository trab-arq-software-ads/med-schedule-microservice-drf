from django_socio_grpc import generics

from appointments.models import Appointment
from appointments.api.serializers import AppointmentProtoSerializer


class AppointmentService(generics.AsyncModelService):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentProtoSerializer
