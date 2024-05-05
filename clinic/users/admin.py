from django.contrib import admin
from .models import User, AddNewMedicalStaff, AddAssistantStaff, Patient

# Register your models here.

admin.site.register(User)
admin.site.register(AddNewMedicalStaff)
admin.site.register(AddAssistantStaff)
admin.site.register(Patient)
