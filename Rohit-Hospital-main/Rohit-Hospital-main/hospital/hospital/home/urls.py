from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   
    path("home",views.home, name='home'),
    path("dlogin",views.dlogin,name='dlogin'),
    path("rlogin",views.rlogin,name='rlogin'),
    path("dregister",views.dregister,name='dregister'),
    path("dhome",views.dhome,name='dhome'),
    path("Rregister",views.Rregister,name='Rregister'),
    path("rhome/",views.rhome,name='rhome'),
    path('search/',views.search_view, name='search_view'),
    path('dhome_success/',views.dhome_success, name='dhome_success'),
    path('rhome_success/',views.rhome_success, name='rhome_success'),
    path('clinical_summary/',views.clinical_summary, name='clinical_summary'),
    path('general_examination/',views.general_examination, name='general_examination'),
    path('diagnosis/',views.diagnosis, name='diagnosis'),
    path('previous_investigation/',views.previous_investigation, name='previous_investigation'),
    path('treatment_in_hospital/',views.treatment_in_hospital, name='treatment_in_hospital'),
    path('clinical_progress/',views.clinical_progress, name='clinical_progress'),
    path('all_patients/',views.all_patients, name='all_patient'),
    path('print_data/',views.print_data, name='print_data'),
    path('prescription/',views.prescription, name='prescription'),
    path('search_tablets/',views.search_tablets, name='prescrisearch_tabletsption'),
    path('save_prescription/',views.save_prescription, name='save_prescription'),
    #path('tablet/',views.tablet, name='tablet'),    
    
    
    
   
    
   
    
]



