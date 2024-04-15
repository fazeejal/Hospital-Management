from django import forms
from .models import Doctor, Patient,Appointment

class DoctorForm(forms.ModelForm):
    # Define status choices
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    # Add new fields to the form
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    specialization = forms.CharField(max_length=100)
    contact_number = forms.CharField(max_length=15)
    is_available = forms.BooleanField(initial=True)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial='pending')

    class Meta:
        model = Doctor
        fields = ['name','username','password', 'specialization', 'contact_number', 'is_available', 'status']
        widgets = {
            'admin_decision': forms.HiddenInput(),  # Hide the admin_decision field
        }
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact_number', 'address', 'medical_history']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date_time', 'status']