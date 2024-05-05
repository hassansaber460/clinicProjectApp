from django.shortcuts import render, HttpResponse
from User.models import Patient, AddAssistantStaff, AddNewMedicalStaff
from .models import Examination, QueueExamination
from django.utils.dateparse import parse_datetime
from django.contrib.auth.decorators import user_passes_test
from .forms import TypeExaminationForm, AdditionalExaminationForm, AnalysisX_RaysForm, MedicineForm


# Create your views here.
def is_superuser(user):
    return user.is_superuser


def is_staff(user):
    return user.is_staff


# @user_passes_test(is_staff)
def indexForAssistant(request):
    examinations = Examination.objects.all()
    sendSignal = False
    return render(request, 'patient/indexForAssistant.html', {'examinations': examinations, 'sendSignal': sendSignal})


def indexForDoctor(request):
    return render(request, 'patient/indexForDoctor.html')


def additionalExamination(request, examination_id):
    examination = Examination.objects.get(examination_id=examination_id)
    if request.method == 'POST':
        form = AdditionalExaminationForm(request.POST)
        if form.is_valid():
            additional_examination = form.save(commit=False)
            additional_examination.examination_id_id = examination_id
            additional_examination.save()
            return HttpResponse('success_url')  # Redirect to a success URL
    else:
        form = AdditionalExaminationForm()
    return render(request, 'patient/additionalExamination.html', {'form': form, 'examination': examination})


def analysisX_rays(request, examination_id):
    examination = Examination.objects.get(examination_id=examination_id)
    if request.method == 'POST':
        form = AnalysisX_RaysForm(request.POST)
        if form.is_valid():
            analysis_X_rays = form.save(commit=False)
            analysis_X_rays.examination_id_id = examination_id
            analysis_X_rays.save()
            form.save_m2m()
            return HttpResponse('success_url')  # Redirect to a success URL
    else:
        form = AnalysisX_RaysForm()
    return render(request, 'patient/analysisXRays.html', {'form': form, 'examination': examination})


def medicines(request, examination_id):
    examination = Examination.objects.get(examination_id=examination_id)
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicines_take = form.save(commit=False)
            medicines_take.examination_id_id = examination_id
            medicines_take.save()
            form.save_m2m()
            return HttpResponse('success_url')  # Redirect to a success URL
    else:
        form = MedicineForm()
    return render(request, 'patient/medicines.html', {'form': form, 'examination': examination})


def response(request, examination_id):
    examination = Examination.objects.get(examination_id=examination_id)
    if request.method == 'POST':
        examination_form = TypeExaminationForm(request.POST)
    else:
        examination_form = TypeExaminationForm()
    return render(request, 'patient/response.html', {'examination': examination,
                                                     'examination_form': examination_form})


def sendExamination(request, examination_id):
    examination = Examination.objects.get(examination_id=examination_id)
    examinations = Examination.objects.all()
    sendSignal = True
    return render(request, 'patient/indexForAssistant.html',
                  {'examination': examination, 'examinations': examinations,
                   'sendSignal': sendSignal})


def getPatient(request):
    patients = Patient.objects.select_related('user_id').all()
    return render(request, 'patient/patient.html', {'patients': patients})


@user_passes_test(is_staff)
def startExamination(request, patient_id):
    patient = Patient.objects.get(patient_id=patient_id)
    assistants = AddAssistantStaff.objects.all()
    doctors = AddNewMedicalStaff.objects.all()
    if request.method == "POST":
        doctor = request.POST.get('doctor', "")
        assistant = request.POST.get('assistant', "")
        examination_date = request.POST.get('examination-date', "")
        type_examination = request.POST.get('type-examination', "")
        Pay = request.POST.get('Pay', "")
        examination_date_parse = parse_datetime(examination_date)
        try:
            medical = AddNewMedicalStaff.objects.get(medicalStaff_id=doctor)
            assistant = AddAssistantStaff.objects.get(medicalStaff_id=assistant)
            examination = Examination.objects.create(patient_id=patient, medical=medical, assistant=assistant,
                                                     type_examination=type_examination,
                                                     examination_date=examination_date_parse,
                                                     pay=Pay)
            QueueExamination.objects.create(examination_id=examination, start_at=examination_date)
        except Exception as e:
            return HttpResponse(f"{e}")

    return render(request, 'patient/start_examination.html', {'patient': patient,
                                                              'assistants': assistants, 'doctors': doctors})
