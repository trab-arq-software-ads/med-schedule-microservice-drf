from django_socio_grpc import proto_serializers
from appointments.models import Appointment
from appointments.grpc.appointments_pb2 import (
    AppointmentResponse,
    AppointmentListResponse,
)

class AppointmentProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Appointment
        fields = ["id", "doctor_id", "patient_id", "date", "symptoms", "diagnosis"]
        proto_class = AppointmentResponse
        proto_class_list = AppointmentListResponse
