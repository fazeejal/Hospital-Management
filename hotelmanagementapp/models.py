from django.db import models
from datetime import datetime

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    medical_history = models.TextField()

    def __str__(self):
        return self.name

from django.db import models

class Doctor(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)  # Add username field
    password = models.CharField(max_length=100,)  # Add password field
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    
    is_available = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    admin_decision = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f"{self.patient.name}'s appointment with Dr. {self.doctor.name} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"
