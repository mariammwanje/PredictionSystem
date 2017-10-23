# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from .models import Patient


class PatientsListView(ListView):
    model = Patient
    template_name = 'patients/patients_list.html'



class PatientCreateView(CreateView):
    model = Patient
    fields = ['name', 'email', 'location','description','assigned_doctor', 'telephone_number']
    success_url = reverse_lazy('patients:patients_list')
    template_name = 'patients/create_patients.html'


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/delete_patients.html'
    success_url = reverse_lazy('patients:patients_list')



class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['name', 'email', 'location','description','assigned_doctor', 'telephone_number']
    # template_name_suffix = '_update_form'
    template_name = 'patients/patients_update.html'

    success_url = reverse_lazy('patients:patients_list')


class PatientDetailView(DetailView):
    model = Patient
    success_url = reverse_lazy('patients:patients_list')
    template_name = 'patients/patients_details.html'

def patients_menu(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients_menu.html', {
        'patients': patients,
    })
