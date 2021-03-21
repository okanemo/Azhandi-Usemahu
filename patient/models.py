from django.db import models

# Create your models here.


class PatientLab(models.Model):
    id_number = models.CharField(max_length=10, primary_key=True)
    patient_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=1)
    date_of_birth = models.CharField(max_length=16)
    lab_number = models.CharField(max_length=128)
    clinic_code = models.CharField(max_length=128)
    date_of_test = models.CharField(max_length=16)
    mobile_phone = models.CharField(max_length=16, default='-')


class LabStudies(models.Model):
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    unit = models.CharField(max_length=128)
    ref_range = models.CharField(max_length=128)
    finding = models.CharField(max_length=1)
    result_state = models.CharField(max_length=1)
