from django.db import models

# Create your models here.
class Appointment(models.Model):
    doctor_id = models.IntegerField()
    patient_id = models.IntegerField()
    date = models.DateTimeField()
    symptoms = models.TextField()
    diagnosis = models.TextField()

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"

    def __str__(self):
        return f"Agendamento {self.pk}"