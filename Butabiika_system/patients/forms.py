from __future__ import unicode_literals
from django.db import models
from django import forms
#from datatables import DataTable
#from django.views.generic import DeleteView


class Patient(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    location = forms.CharField(max_length=100)
    description = forms.TextField(max_length=1000, blank=True)
    assigned_doctor = forms.ForeignKey(Doctor)
    telephone_number = forms.IntegerField()
