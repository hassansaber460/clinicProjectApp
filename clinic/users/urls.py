from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('addPatient/', views.register, name='addPatient'),
    path('Addmedicalstaff/', views.addMedicalStaff, name='Addmedicalstaff'),
    path('edit/', views.editProfileDoctor, name='edit'),
    path('editPatient/<int:patient_id>', views.editPatient, name='editPatient')
]
