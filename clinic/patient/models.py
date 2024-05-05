from django.db import models

from users.models import Patient, AddNewMedicalStaff, AddAssistantStaff


# Create your models here.


class Examination(models.Model):
    examination_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical = models.ForeignKey(AddNewMedicalStaff, on_delete=models.CASCADE)
    assistant = models.ForeignKey(AddAssistantStaff, on_delete=models.CASCADE)
    type_examination = models.TextField()
    examination_date = models.DateField()
    pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.patient_id.user_id.firstname} {self.patient_id.user_id.lastname}"


class QueueExamination(models.Model):
    examination_id = models.OneToOneField(Examination, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(null=True)
    activate = models.BooleanField(default=False)

    def __str__(self):
        return self.examination_id.patient_id.user_id.ssn


class AdditionalExamination(models.Model):
    examination_id = models.ForeignKey(Examination, on_delete=models.CASCADE)
    additional_examination = models.TextField()
    pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.examination_id.patient_id.user_id.firstname} {self.examination_id.patient_id.user_id.lastname}"


class MedicineName(models.Model):
    promo_code = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.medicine_name


class Medicine(models.Model):
    examination_id = models.ForeignKey(Examination, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(MedicineName, related_name='posts_liked', blank=True)
    pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.examination_id.patient_id.user_id.firstname} {self.examination_id.patient_id.user_id.lastname}"


class AnalysisName(models.Model):
    Analysis_id = models.AutoField(primary_key=True)
    analysis_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.analysis_name


class AnalysisX_ray(models.Model):
    examination_id = models.ForeignKey(Examination, on_delete=models.CASCADE)
    analysis = models.ManyToManyField(AnalysisName, related_name='analysis')
    pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.examination_id.patient_id.user_id.firstname} {self.examination_id.patient_id.user_id.lastname}"


class TypeExamination(models.Model):
    examination_id = models.ForeignKey(Examination, on_delete=models.CASCADE)
    height = models.PositiveIntegerField()
    temperature = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    hear_beat = models.PositiveIntegerField()
    hypertension = models.PositiveIntegerField()
    low_blood_pressure = models.PositiveIntegerField()
    head_circumference = models.PositiveIntegerField()
    medical_diagnosis = models.TextField()
    reexamination_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.examination_id.patient_id.user_id.firstname} {self.examination_id.patient_id.user_id.lastname}"
