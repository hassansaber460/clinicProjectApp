from django.shortcuts import render
from .forms import PatientForm, MedicalStaffForm, ProfileEditForm, UserEditForm
from django.http import HttpResponse
from .models import Patient, AddNewMedicalStaff, AddAssistantStaff
import logging
from .models import User as Profile
from django.contrib.auth.models import User as userDjango

# Create your views here.
logger = logging.getLogger(__name__)


def register(request):
    if request.method == 'POST':
        user_form = PatientForm(request.POST)
        if user_form.is_valid():
            try:
                # If the form is valid, save the data to the database
                company_name = user_form.cleaned_data['company']
                new_user = user_form.save()
                try:
                    Patient.objects.create(user_id=new_user, company_name=company_name)
                    return HttpResponse(f"ll")
                except Exception as e:
                    return HttpResponse(e)

            except Exception as e:
                logger.error("Error saving user: %s", e)
                return HttpResponse('Error saving user data', status=500)
    else:
        user_form = PatientForm()
    return render(request, 'User/addPatient.html', {'user_form': user_form})


def addMedicalStaff(request):
    if request.method == 'POST':
        user_form = MedicalStaffForm(request.POST)
        if user_form.is_valid():
            try:
                user_name = user_form.cleaned_data['user_name']
                email = user_form.cleaned_data['email']
                password = user_form.cleaned_data['password']
                confirm_password = user_form.cleaned_data['confirm_password']
                staff_type = user_form.cleaned_data['staff_type']
                if password != confirm_password:
                    return HttpResponse("password not matching")
                else:
                    try:

                        if staff_type == "D":
                            new_user = userDjango.objects.create_user(username=user_name, email=email,
                                                                      password=password,
                                                                      is_staff=True, is_superuser=True)
                            user_create = user_form.save()
                            AddNewMedicalStaff.objects.create(user=new_user, user_create=user_create)
                        elif staff_type == "A":
                            new_user = userDjango.objects.create_user(username=user_name, email=email,
                                                                      password=password,
                                                                      is_staff=True, is_superuser=False)
                            user_create = user_form.save()
                            AddAssistantStaff.objects.create(user=new_user, user_create=user_create)
                    except Exception as e:
                        return HttpResponse(f"{e}-->{staff_type}")

            except Exception as e:
                logger.error("Error saving user: %s", e)
                return HttpResponse('Error saving user data', status=500)

    else:
        user_form = MedicalStaffForm()

    return render(request, 'User/Addmedicalstaff.html',
                  {'user_form': user_form})


def editProfileDoctor(request):
    user = AddNewMedicalStaff.objects.get(user=request.user).user_create
    user_profile = Profile.objects.get(user_id=user.user_id)
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=user_profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.email = user_form.cleaned_data['email']
            user_form.save()
            profile.save()
            return HttpResponse("success")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=user_profile)
    return render(request, 'User/edit.html', {'user_form': user_form, 'profile_form': profile_form})
