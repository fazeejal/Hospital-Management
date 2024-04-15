from django.shortcuts import render,redirect,get_object_or_404
from .models import Patient, Doctor, Appointment
from .forms import DoctorForm, PatientForm, AppointmentForm
from django.contrib import messages


def dashboard(request):
    # Fetch data for the dashboard
    total_patients = Patient.objects.count()
   
    pending_appointments = Appointment.objects.filter(status='Pending').count()

    total_doctors = Doctor.objects.count()
    available_doctors = Doctor.objects.filter(is_available=True).count()
    

    total_appointments = Appointment.objects.count()
    completed_appointments = Appointment.objects.filter(status='Completed').count()
    

    context = {
        'total_patients': total_patients,
       
        'pending_appointments': pending_appointments,
        'total_doctors': total_doctors,
        'available_doctors': available_doctors,
        
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        
    }
    return render(request, 'dashboard.html', context)

def patient_list(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patient_list.html', context)

def doctor_list(request):
    doctors = Doctor.objects.filter(status='approved')  # Only fetch approved doctors
    context = {'doctors': doctors}
    return render(request, 'doctor_list.html', context)

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.status = 'pending'  # Set status to pending initially
            doctor.save()
            return redirect('admin_dashboard')  # Redirect to admin dashboard after adding a doctor
    else:
        form = DoctorForm()
    return render(request, 'add_doctor.html', {'form': form})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after adding a patient
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after adding an appointment
    else:
        form = AppointmentForm()
    return render(request, 'add_appointment.html', {'form': form})


def admin_dashboard(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    doctor_requests = Doctor.objects.filter(status='pending')

    context = {
        'doctors': doctors,
        'patients': patients,
        'doctor_requests': doctor_requests,
    }
    return render(request, 'admin/admin_dashboard.html',context)

from django.shortcuts import get_object_or_404, redirect

def accept_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    doctor.status = 'approved'
    doctor.save()
    return redirect('admin_dashboard')

def reject_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    doctor.status = 'rejected'
    doctor.save()
    doctor.delete()
    return redirect('admin_dashboard')



def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        # Check if the user is an admin
        if name == "admin" and password == "1234":
            request.session['admin'] = 'admin'
            request.session['adminname'] = name
            request.session['adminpswd'] = password
            return redirect('admin_dashboard')  # Redirect to admin dashboard
        # Check if the user is a doctor
        elif Doctor.objects.filter(name=name, password=password).exists():
            doctor = Doctor.objects.get(name=name, password=password)
            request.session['uid'] = doctor.id
            request.session['username'] = name
            request.session['userpswd'] = password
            return redirect('doctor_view')  # Redirect to doctor view page
        else:
            messages.error(request, 'Invalid username or password.')  # Display error message
            return render(request, 'login.html')

    return render(request, 'login.html')


def doctor_view(request):
    # Retrieve doctor's data based on session information
    doctor_id = request.session.get('uid')
    doctor = Doctor.objects.get(id=doctor_id)  # Assuming doctor ID is stored in session
    context = {'doctor': doctor}
    return render(request, 'doctor_view.html', context)

def delete_doctor(request, doctor_id):
    if request.method == 'POST':
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            doctor.delete()
            messages.success(request, 'Doctor deleted successfully.')
        except Doctor.DoesNotExist:
            messages.error(request, 'Doctor not found.')
    return redirect('admin_dashboard')  # Redirect to your admin dashboard URL

def delete_patient(request, patient_id):
    if request.method == 'POST':
        try:
            patient = Patient.objects.get(id=patient_id)
            patient.delete()
            messages.success(request, 'Patient deleted successfully.')
        except Patient.DoesNotExist:
            messages.error(request, 'Patient not found.')
    return redirect('admin_dashboard')  # Redirect to your admin dashboard URL