from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.PatientsListView.as_view(), name='patients_list'),
    url(r"patients/(?P<pk>\d+)/$", views.PatientCreateView.as_view(), name='patients_details'),
    url(r"patients/(?P<pk>\d+)/update/$", views.PatientUpdateView.as_view(), name='patients_update'),
    url(r"patients/(?P<pk>\d+)/delete/$", views.PatientDeleteView.as_view(), name='delete_patients'),
    url(r"patients/create/$", views.PatientCreateView.as_view(), name='create_patients'),
]
