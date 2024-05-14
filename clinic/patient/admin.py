from django.contrib import admin
from .models import (Examination, QueueExamination, AdditionalExamination, MedicineName,
                     Medicine, AnalysisName, AnalysisX_ray, TypeExamination)

# Register your models here.

admin.site.register(Examination)
admin.site.register(QueueExamination)
admin.site.register(AdditionalExamination)
admin.site.register(MedicineName)
admin.site.register(Medicine)
admin.site.register(AnalysisName)
admin.site.register(AnalysisX_ray)
admin.site.register(TypeExamination)

