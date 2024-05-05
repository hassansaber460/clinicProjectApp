from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    user_id = models.AutoField(primary_key=True)
    ssn = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    family_name = models.CharField(max_length=15, null=True)
    date_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    province = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=11)
    photo_user = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f"{self.ssn}"


class AddNewMedicalStaff(models.Model):
    medicalStaff_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_create = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class AddAssistantStaff(models.Model):
    medicalStaff_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_create = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    patient_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient_id} {self.user_id.firstname} {self.user_id.ssn}"
