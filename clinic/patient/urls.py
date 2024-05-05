from . import views
from django.urls import path

urlpatterns = [
    path('patient/', views.getPatient, name='patient'),
    path('indexForAssistant/', views.indexForAssistant, name='indexForAssistant'),
    path('indexForDoctor/', views.indexForDoctor, name='indexForDoctor'),
    path('<int:patient_id>/', views.startExamination, name="startExamination"),
    path('indexForAssistant/<int:examination_id>/', views.sendExamination, name="sendExamination"),
    path('response/<int:examination_id>/', views.response, name="response"),
    path('add_additional_examination/<int:examination_id>/', views.additionalExamination,
         name='add_additional_examination'),
    path('analysisX_Rays/<int:examination_id>/', views.analysisX_rays,
         name='analysisX_Rays'),
    path('medicines/<int:examination_id>/', views.medicines,
         name='medicines')
]
