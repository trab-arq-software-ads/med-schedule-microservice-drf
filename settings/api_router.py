from rest_framework import routers

from appointments.api.viewsets import AppointmentViewSet

router = routers.SimpleRouter()
router.register(r"appointments", AppointmentViewSet)
