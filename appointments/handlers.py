# quickstart/handlers.py
from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry

from appointments.services import AppointmentService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("appointments", server)
    app_registry.register(AppointmentService)
