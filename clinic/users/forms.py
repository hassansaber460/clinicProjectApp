from django import forms
from .models import User, Patient
from datetime import datetime
from django.contrib.auth.models import User as user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': "form-control",
                       'placeholder': "google", 'type': 'email'})
        }


class UserForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES,
                               widget=forms.RadioSelect(attrs={'class': 'gender-radio'}))

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'ssn': forms.TextInput(attrs={'type': "text",
                                          'class': "form-control",
                                          'placeholder': "000000 000 00 000",
                                          }),
            'email': forms.EmailInput(
                attrs={'class': "form-control",
                       'placeholder': "google", 'type': 'email'}),
            'firstname': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control",
                       'placeholder': "First Name"}
            ),
            'lastname': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control ",
                       'placeholder': "Last Name"}
            ),
            'family_name': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control",
                       'placeholder': "Family Name"}
            ),
            'date_birth': forms.DateInput(
                attrs={'type': "date",
                       'class': "form-control"}
            ),
            'country': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control", 'placeholder': "Country"}
            ),
            'province': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control", 'placeholder': "Province"}
            ),
            'city': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control", 'placeholder': "City"}
            ),
            'phone_number': forms.TextInput(attrs={'type': "text",
                                                   'class': "form-control", 'placeholder': "Phone Number"}),

        }
        abstract = True

    def clean_date(self):

        try:
            date_obj = datetime.strptime(self.cleaned_data['date_birth'], '%d/%m/%Y').date()
            return date_obj
        except ValueError:
            raise forms.ValidationError('تنسيق التاريخ غير صالح. يجب أن يكون بتنسيق dd/mm/yyyy.')


class PatientForm(UserForm, forms.ModelForm):
    company = forms.CharField(label='Company', widget=forms.TextInput(
        attrs={'type': 'text', 'class': "form-control",
               'placeholder': "ACME Inc."}
    ))


class MedicalStaffForm(UserForm, forms.ModelForm):
    STAFF_CHOICES = (
        ('A', 'assistant'),
        ('D', 'doctor'),
    )
    staff_type = forms.ChoiceField(label='staffType', choices=STAFF_CHOICES,
                                   widget=forms.RadioSelect(attrs={'class': 'gender-radio'}))
    user_name = forms.CharField(label='username', widget=forms.TextInput(
        attrs={
            'type': "text",
            'class': "form-control",
            'id': "username",
            'name': "username",
            'placeholder': "Enter your username",
            'autofocus': True
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'type': "password",
            'id': "password",
            'class': "form-control",
            'name': "password",
            'aria-describedby': "password", }
    ))
    confirm_password = forms.CharField(label='Confirm_Password', widget=forms.PasswordInput(
        attrs={
            'type': "password",
            'id': "Confirm_Password",
            'class': "form-control",
            'name': "Confirm_Password",
            'aria-describedby': "Confirm_Password", }
    ))


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'family_name', 'province', 'city', 'country', 'phone_number', 'photo_user')
        widgets = {
            'firstname': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control",
                       'placeholder': "First Name"}
            ),
            'lastname': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control ",
                       'placeholder': "Last Name"}
            ),
            'family_name': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control",
                       'placeholder': "Family Name"}
            ),
            'country': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control", 'placeholder': "Country"}
            ),
            'province': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control", 'placeholder': "Province"}
            ),
            'city': forms.TextInput(
                attrs={'type': "text",
                       'class': "form-control", 'placeholder': "City"}
            ),
            'phone_number': forms.TextInput(attrs={'type': "text",
                                                   'class': "form-control", 'placeholder': "Phone Number"}),

        }


class EditPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('company_name',)

    company_name = forms.CharField(label='Company', widget=forms.TextInput(
        attrs={'type': 'text', 'class': "form-control",
               'placeholder': "ACME Inc."}
    ))
