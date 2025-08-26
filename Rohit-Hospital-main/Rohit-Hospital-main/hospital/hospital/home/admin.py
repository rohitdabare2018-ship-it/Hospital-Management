from django.contrib import admin
from home.models import Prescription,Tablet,Doctors,Receptionist,Patient,temp,clinical_summary_data,general_examination_data,diagnosis_data,previous_investigation_data,treatment_in_hospital_data,clinical_progress_data

# Register your models here.
admin.site.register(Doctors)
admin.site.register(Receptionist)
admin.site.register(Patient)
admin.site.register(temp)
admin.site.register(clinical_summary_data)
admin.site.register(general_examination_data)
admin.site.register(diagnosis_data)
admin.site.register(previous_investigation_data)
admin.site.register(treatment_in_hospital_data)
admin.site.register(clinical_progress_data)
admin.site.register(Tablet)
admin.site.register(Prescription)