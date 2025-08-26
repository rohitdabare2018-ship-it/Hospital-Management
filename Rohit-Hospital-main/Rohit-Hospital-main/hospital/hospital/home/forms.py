from django import forms
from home.models import Tablet,Doctors,Receptionist,Patient,temp,clinical_summary_data,general_examination_data,diagnosis_data,previous_investigation_data,treatment_in_hospital_data,clinical_progress_data

class User(forms.Form):
    name=forms.CharField()
    age=forms.CharField()


class clinical_summary_form(forms.ModelForm):
    class Meta:
        model = clinical_summary_data  # Adjust the model according to your needs
        fields = [ 'injection', 'saline', 'description']# Include the fields you want to display/edit

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            # Update the form fields with the instance data
            #self.fields['patient_id'].initial = instance.patient_id
            #self.fields['patient_name'].initial = instance.patient_name
            self.fields['injection'].initial = instance.injection
            self.fields['saline'].initial = instance.saline
            self.fields['description'].initial = instance.description
            
class general_examination_form(forms.ModelForm):
    class Meta:
        model = general_examination_data  # Adjust the model according to your needs
        fields = [ 'Blood_Pressure', 'Temperature', 'Height','Sugar_level']# Include the fields you want to display/edit

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            # Update the form fields with the instance data
            #self.fields['patient_id'].initial = instance.patient_id
            #self.fields['patient_name'].initial = instance.patient_name
            self.fields['Blood_Pressure'].initial = instance.Blood_Pressure
            self.fields['Temperature'].initial = instance.Temperature
            self.fields['Height'].initial = instance.Height
            self.fields['Sugar_level'].initial = instance.Sugar_level


class diagnosis_form(forms.ModelForm):
    class Meta:
        model = diagnosis_data  # Adjust the model according to your needs
        fields = [ 'Details']# Include the fields you want to display/edit

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            # Update the form fields with the instance data
            #self.fields['patient_id'].initial = instance.patient_id
            #self.fields['patient_name'].initial = instance.patient_name
            self.fields['Details'].initial = instance.Details
                      


class previous_investigation_form(forms.ModelForm):
    class Meta:
        model = previous_investigation_data  # Adjust the model according to your needs
        fields = [ 'Details']# Include the fields you want to display/edit

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            # Update the form fields with the instance data
            #self.fields['patient_id'].initial = instance.patient_id
            #self.fields['patient_name'].initial = instance.patient_name
            self.fields['Details'].initial = instance.Details



class treatment_in_hospital_form(forms.ModelForm):
    class Meta:
        model = treatment_in_hospital_data  # Adjust the model according to your needs
        fields = [ 'Details']# Include the fields you want to display/edit

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            # Update the form fields with the instance data
            #self.fields['patient_id'].initial = instance.patient_id
           # self.fields['patient_name'].initial = instance.patient_name
            self.fields['Details'].initial = instance.Details

class clinical_progress_form(forms.ModelForm):
    class Meta:
        model = clinical_progress_data  # Adjust the model according to your needs
        fields = ['Details']# Include the fields you want to display/edit

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            # Update the form fields with the instance data
            #self.fields['patient_id'].initial = instance.patient_id
           # self.fields['patient_name'].initial = instance.patient_name
            self.fields['Details'].initial = instance.Details


class PrescriptionForm(forms.Form):
    tablet = forms.ModelChoiceField(queryset=Tablet.objects.all())
    timing = forms.CharField(max_length=100)