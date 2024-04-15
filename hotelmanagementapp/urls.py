from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('accept_doctor/<int:doctor_id>/', views.accept_doctor, name='accept_doctor'),
    path('reject_doctor/<int:doctor_id>/', views.reject_doctor, name='reject_doctor'),
    path('patients/', views.patient_list, name='patient_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('login/', views.login, name='login'),  # URL for the login view
    path('doctor_view/', views.doctor_view, name='doctor_view'),
    path('delete_doctor/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient'),
]
