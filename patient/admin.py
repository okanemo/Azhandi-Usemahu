from django.contrib import admin

# Register your models here.
from .models import PatientLab, LabStudies

admin.site.register(PatientLab)
admin.site.register(LabStudies)
