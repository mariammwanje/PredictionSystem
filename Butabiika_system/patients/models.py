from django.db import models
from doctors.models import Doctor

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    assigned_doctor = models.ForeignKey(Doctor)
    telephone_number = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class CreatePatient(models.Model):
    model = Patient
    fields = ['name', 'email', 'location','description','assigned_doctor', 'telephone_number']


class DeletePatient(models.Model):
    model = Patient


class UpdatePatient(models.Model):
    model = Patient
    fields = ['name', 'email', 'location','description','assigned_doctor', 'telephone_number']

# class Prediction(models.Model):
