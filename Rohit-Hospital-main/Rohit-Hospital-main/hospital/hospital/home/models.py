from django.db import models

# Create your models here.

class Doctors(models.Model):
    GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]
    name=models.CharField(max_length=122)
    dob=models.DateField()
    designation=models.CharField(max_length=122)
    department=models.CharField(max_length=122)
    mln=models.CharField(max_length=20)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone=models.CharField(max_length=122)
    email=models.EmailField(unique=True)
    address=models.TextField(max_length=200)
    password=models.CharField(max_length=128)

    def __str__(self):
        return self.name
    

class Receptionist(models.Model):
    GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]
    name=models.CharField(max_length=122)
    dob=models.DateField()
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone=models.CharField(max_length=122)
    email=models.EmailField(unique=True)
    address=models.TextField(max_length=200)
    password=models.CharField(max_length=128)

    def __str__(self):
        return self.name
    

class Patient(models.Model):
    GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]
    
    
    
    patient_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=122)
    age=models.CharField(max_length=122)
    weight=models.CharField(max_length=122)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    admission_date=models.DateField()
    time=models.TimeField()
    phone=models.CharField(max_length=122)
    address=models.TextField(max_length=200)
    
    def __str__(self):
        return f"{self.patient_id} - {self.name}"


class temp(models.Model):
    name=models.CharField(max_length=122)
    age=models.CharField(max_length=122)    
    def __str__(self):
        return self.name
    

class clinical_summary_data(models.Model):
    patient_id=models.CharField(max_length=122)
    patient_name=models.CharField(max_length=122)
    injection=models.CharField(max_length=122)
    saline=models.CharField(max_length=122)   
    description=models.CharField(max_length=1222)  
    def __str__(self):
        return self.patient_id


class general_examination_data(models.Model):
    patient_id=models.CharField(max_length=122)
    patient_name=models.CharField(max_length=122)
    Blood_Pressure=models.CharField(max_length=122)
    Temperature=models.CharField(max_length=122)   
    Height=models.CharField(max_length=122)  
    Sugar_level=models.CharField(max_length=122)  

    def __str__(self):
        return self.patient_id


class diagnosis_data(models.Model):
    patient_id=models.CharField(max_length=122)
    patient_name=models.CharField(max_length=122)
    Details=models.CharField(max_length=1222)
    def __str__(self):
        return self.patient_id


class previous_investigation_data(models.Model):
    patient_id=models.CharField(max_length=122)
    patient_name=models.CharField(max_length=122)
    Details=models.CharField(max_length=1222)
    def __str__(self):
        return self.patient_id
    

class treatment_in_hospital_data(models.Model):
    patient_id=models.CharField(max_length=122)
    patient_name=models.CharField(max_length=122)
    Details=models.CharField(max_length=1222)
    def __str__(self):
        return self.patient_id
    

class clinical_progress_data(models.Model):
    patient_id=models.CharField(max_length=122)
    patient_name=models.CharField(max_length=122)
    Details=models.CharField(max_length=1222)
    def __str__(self):
        return self.patient_id
    



class Tablet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    tablet=models.CharField(max_length=122)
    patient_id=models.CharField(max_length=122)
    patient_name=models.CharField(max_length=122)
    morning = models.IntegerField(default=0)
    afternoon = models.IntegerField(default=0)
    evening = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.patient_id} - {self.patient_name}"