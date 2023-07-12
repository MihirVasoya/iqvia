from django.db import models
class Patient(models.Model):
    patientId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    contactNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    # Add other fields as per your requirements

    def __str__(self):
        return self.name
# Create your models here.
