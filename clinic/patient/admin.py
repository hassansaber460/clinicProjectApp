from django.contrib import admin
from .models import (QueueExamination, Examination, TypeExamination, AdditionalExamination, MedicineName, AnalysisName,
                     Medicine, AnalysisX_ray)

# Register your models here.

admin.site.register(QueueExamination)
admin.site.register(Examination)
admin.site.register(TypeExamination)
admin.site.register(AdditionalExamination)
admin.site.register(MedicineName)
admin.site.register(AnalysisName)
admin.site.register(Medicine)
admin.site.register(AnalysisX_ray)
