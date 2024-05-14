from django import forms
from .models import TypeExamination, AdditionalExamination, AnalysisX_ray, Medicine
from datetime import datetime


class TypeExaminationForm(forms.ModelForm):
    class Meta:
        model = TypeExamination
        fields = ['height', 'temperature', 'weight', 'hear_beat', 'hypertension',
                  'low_blood_pressure', 'head_circumference', 'medical_diagnosis', 'reexamination_date']
        widgets = {
            'height': forms.TextInput(attrs={'type': "number",
                                             'class': "form-control",
                                             'placeholder': "170 cm",
                                             }),
            'temperature': forms.EmailInput(
                attrs={'class': "form-control",
                       'placeholder': "37 c", 'type': 'number'}),
            'weight': forms.TextInput(
                attrs={'type': "number",
                       'class': "form-control",
                       'placeholder': "75 Kg"}
            ),
            'hear_beat': forms.TextInput(
                attrs={'type': "number",
                       'class': "form-control ",
                       'placeholder': "hear_beat"}
            ),
            'hypertension': forms.TextInput(
                attrs={'type': "number",
                       'class': "form-control",
                       'placeholder': "hypertension"}
            ),
            'low_blood_pressure': forms.DateInput(
                attrs={'type': "number",
                       'class': "form-control"
                    , 'placeholder': "low_blood_pressure"}
            ),
            'head_circumference': forms.TextInput(
                attrs={'type': "number",
                       'class': "form-control", 'head_circumference': "head_circumference"}
            ),
            'medical_diagnosis': forms.Textarea(
                attrs={'type': "text",
                       'class': "form-control", 'placeholder': "medical_diagnosis"}
            ),
            'reexamination_date': forms.TextInput(
                attrs={'type': "date",
                       'class': "form-control"}
            )

        }

    def clean_date(self):

        try:
            date_obj = datetime.strptime(self.cleaned_data['date_birth'], '%d/%m/%Y').date()
            return date_obj
        except ValueError:
            raise forms.ValidationError('تنسيق التاريخ غير صالح. يجب أن يكون بتنسيق dd/mm/yyyy.')


class AdditionalExaminationForm(forms.ModelForm):
    class Meta:
        model = AdditionalExamination
        fields = ['additional_examination', 'pay']
        widgets = {
            'additional_examination': forms.Textarea(
                attrs={'type': "text",
                       'class': "form-control", 'placeholder': "additional examination"}
            ),
            'pay': forms.NumberInput(attrs={'type': "number", 'class': "form-control", 'step': 'any'})
        }


class AnalysisX_RaysForm(forms.ModelForm):
    class Meta:
        model = AnalysisX_ray
        fields = ['analysis', 'pay']
        widgets = {
            'analysis': forms.CheckboxSelectMultiple,
            'pay': forms.NumberInput(attrs={'type': "number", 'class': "form-control", 'step': 'any'})
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['medicine', 'pay']
        widgets = {
            'medicine': forms.CheckboxSelectMultiple,
            'pay': forms.NumberInput(attrs={'type': "number", 'class': "form-control", 'step': 'any'})
        }
