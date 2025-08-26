from django.shortcuts import render,HttpResponse,redirect
from home.models import Prescription,Tablet,Doctors,Receptionist,Patient,temp,clinical_summary_data,general_examination_data,diagnosis_data,previous_investigation_data,treatment_in_hospital_data,clinical_progress_data
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import User,clinical_summary_form,general_examination_form,diagnosis_form,previous_investigation_form,treatment_in_hospital_form,clinical_progress_form
from django.http import JsonResponse
import json



# Create your views here.
def home(request):
    form=User()
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        print(name,age)
        t=temp(name=name,age=age)
        t.save()

    return render(request,'base.html',{'form':form})


'''def home(request):
    return render(request,'index.html')
extraaaa thing
    #return HttpResponse("This is home page")'''

def dlogin(request):
    return render(request,'dlogin.html')

def rlogin(request):
    return render(request,'rlogin.html')

def dregister(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        designation=request.POST.get('designation')
        department=request.POST.get('department')
        mln=request.POST.get('mln')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        password=request.POST.get('password')

        doctors=Doctors(name=name,dob=dob,designation=designation,department=department,mln=mln,gender=gender,
                        phone=phone,email=email,address=address,password=password)
        doctors.save()
        messages.success(request, "You are registered successfully!You can login now.")


    return render(request,'dregister.html')
    

def dhome(request):
    if request.method == "POST":
        if 'docUsername' in request.POST and 'docPassword' in request.POST:
            demail=request.session.get('docUsername')    
            email=request.POST.get('docUsername')
            password=request.POST.get('docPassword')
            try:
                doctor = Doctors.objects.get(email=email)
                doctor=Doctors.objects.get(email=email)
                demail=doctor.email
                dpassword=doctor.password
                dname=doctor.name
                if (email==demail) and (password==dpassword):
                    request.session['demail']=doctor.email
                    return render(request,'dhome.html',{'dname':dname})
                else:
                    return render(request,'dlogin.html',{'error':"Enter correct Username or Password"})
                    #return HttpResponse("enter correct username or password")
            except Doctors.DoesNotExist:
                return render(request,'dlogin.html',{'error':"Your are not registerd. Please Register"})

                #return HttpResponse("Your are not registerd. Please Register")
            

        elif 'name' in request.POST and 'age' in request.POST:
            demail=request.session.get('demail')
            doctor=Doctors.objects.get(email=demail)
            dname=doctor.name
            
            name=request.POST.get('name')
            age=request.POST.get('age')
            weight=request.POST.get('weight')
            gender=request.POST.get('gender')
            adate=request.POST.get('admission_date')
            time=request.POST.get('time')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            patient=Patient(name=name,age=age,weight=weight,gender=gender,admission_date=adate,time=time,phone=phone,address=address)
            patient.save()
            patient_id= Patient.objects.order_by('-patient_id').first().patient_id
            context={'dname':dname,'patient_id':patient_id}
            messages.success(request, "You'r Appointment booked successfully.your Patient ID is:"+str(patient_id))
            return redirect('dhome_success')
    
    
    
    
    else:
        demail=request.session.get('demail')
        doctor=Doctors.objects.get(email=demail)
        dname=doctor.name
        
        return render(request,'dhome.html',{'dname':dname})  









def dhome_success(request):
    demail=request.session.get('demail')
    doctor=Doctors.objects.get(email=demail)
    dname=doctor.name
    # Retrieve patient details or perform any additional processing if needed
    if request.method == 'GET':
        query = request.GET.get('query')
       
        if query:
            request.session['current_patient_id'] = query
            print("Rquery:", query)
            
            
           
           
                #print("id=",patient.patient_id)
           
            results = Patient.objects.filter(patient_id=query).values()
            

            print("result from dhome :", results)
            if results:
                   
                results_list = list(results)
                
                return JsonResponse({'results_list': results_list}, safe=False)
                
            else:
                return JsonResponse([], safe=False)
        else:
            # Handle case where no query parameter is provided
            return JsonResponse({'error': 'Invalid request. Please provide a query parameter.'}, safe=False)
    
        #return JsonResponse({'error': 'Method not allowed: GET required.'}, safe=False)

    # Render a success page with patient details
    return render(request, 'dhome.html', {'dname':dname})

        #password verification
    '''user=authenticate(email=email,password=password)
        print(email,password)
        print(user)
        if user is not None:
            return HttpResponse("welcome Doctor")
        else:
            #return HttpResponse(username,password)
            return HttpResponse("enter correct username or password")
    
        #email=Doctors.objects.get(email=username)
        #pas=Doctors.objects.get(email=username)'''







def Rregister(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        password=request.POST.get('password')
        receptionist=Receptionist(name=name,dob=dob,gender=gender,phone=phone,email=email,address=address,password=password)
        receptionist.save()
        messages.success(request, "You are registered successfully!You can login now.")

    return render(request,'Rregister.html')



def rhome(request):
    
    if request.method == "POST":
        if 'rUsername' in request.POST and 'rPassword' in request.POST:
        # Receptionist Login
            remail=request.session.get('rUsername') 
            email = request.POST.get('rUsername')
            password = request.POST.get('rPassword')
            try:
                receptionist = Receptionist.objects.get(email=email)
                remail = receptionist.email
                rpassword = receptionist.password
                rname = receptionist.name

                if email == remail and password == rpassword:
                    request.session['remail']=receptionist.email

                    return render(request, 'rhome.html', {'rname': rname})

        # Patient Registration
                else:
                    return render(request,'rlogin.html',{'error':'Invalid Login Credentials!'}) 
            except Receptionist.DoesNotExist:
            # Handle case where Receptionist with specified query does not exist
                return render(request, 'rlogin.html', {'error': 'Receptionist not found.'})
    
        elif 'name' in request.POST and 'age' in request.POST:
            remail=request.session.get('remail')
            receptionist=Receptionist.objects.get(email=remail)
            rname=receptionist.name
            name=request.POST.get('name')
            age=request.POST.get('age')
            weight=request.POST.get('weight')
            gender=request.POST.get('gender')
            adate=request.POST.get('admission_date')
            time=request.POST.get('time')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            patient=Patient(name=name,age=age,weight=weight,gender=gender,admission_date=adate,time=time,phone=phone,address=address)
            patient.save()
            patient_id= Patient.objects.order_by('-patient_id').first().patient_id
            context={'dname':rname,'patient_id':patient_id}
            messages.success(request, "You'r Appointment booked successfully.your Patient ID is:"+str(patient_id))
            return redirect('rhome_success')
           
      


    elif request.method == 'GET':
        
        query = request.GET.get('query')
        if query:
            print("Rquery:", query)
            results = Patient.objects.filter(patient_id=query).values()
            print("result from rhome:", results)
            if results:
                results_list = list(results)
                return JsonResponse({'results_list': results_list}, safe=False)
               
            else:
                return JsonResponse([], safe=False)
        else:
            # Handle case where no query parameter is provided
            return JsonResponse({'error': 'Invalid request. Please provide a query parameter.'}, safe=False)
    
        #return JsonResponse({'error': 'Method not allowed: GET required.'}, safe=False)
    

    else:
        remail=request.session.get('remail')
        receptionist=Receptionist.objects.get(email=remail)
        rname=receptionist.name
        return render(request,'rhome.html',{'rname':rname})
    
    #return render(request, 'rhome.html', {'rname': rname, 'results': results,'query': query})
    #receptionist = Receptionist.objects.get()
    #rname = receptionist.name
    #return render(request, 'rhome.html',{'rname': rname})






    






    #replaced with above code
    '''if request.method=="POST":
        email=request.POST.get('rUsername')
        password=request.POST.get('rPassword')
        try:
            receptionist = Receptionist.objects.get(email=email)
        except Receptionist.DoesNotExist:
            return HttpResponse("Receptionist with the given email does not exist.")
        receptionist=Receptionist.objects.get(email=email)
        remail=receptionist.email
        rpassword=receptionist.password
        rname=receptionist.name
        if (email==remail) and (password==rpassword):
            return render(request,'rhome.html',{'rname':rname}) '''
    '''else:((extraa try catch block added behalf of this))
            return HttpResponse("enter correct username or password")'''
    
 
def rhome_success(request ):
    remail=request.session.get('remail')
    receptionist=Receptionist.objects.get(email=remail)
    rname=receptionist.name
    # Retrieve patient details or perform any additional processing if needed
    # ...

    # Render a success page with patient details
    return render(request, 'rhome.html', {'rname':rname})


    #searchbar
def search_view(request):

    query = request.GET.get('query', '')


    if query:
        print("Query:", query)
    # Use values() to get the entire record
        results = Patient.objects.filter(patient_id=query).values()
    else:
        results = []

    print("Results:", results)
    return render(request, 'search.html', {'results': results})

    '''print("Search view called")
    query = request.GET.get('query', '')

    if query:
        print("Query:", query)
        # Use values() to get the entire record
        results = Receptionist.objects.filter(name__icontains=query).values()
    else:
        results = []

    print("Results:", results)
    return render(request, 'search.html', {'results': results}) '''


def clinical_summary(request):
  demail = request.session.get('demail')
  patient_id = request.session.get('current_patient_id')

  patient=Patient.objects.get(patient_id=patient_id)
  patient_name=patient.name
  # Retrieve existing clinical summary data for the patient
  try:
    summary_data = clinical_summary_data.objects.get(patient_id=patient_id)
  except clinical_summary_data.DoesNotExist:
    summary_data = None

  doctor = Doctors.objects.get(email=demail)
  dname = doctor.name
  patient=Patient.objects.get(patient_id=patient_id)
  patient_name=patient.name


  if request.method == "POST":
    # Create a dictionary containing patient_id and patient_name
    post_data = request.POST.copy()
    post_data['patient_id'] = patient_id
    post_data['patient_name'] = patient_name

    # Bind form with the modified POST data
    form = clinical_summary_form(post_data, instance=summary_data)
    if form.is_valid():
      form.save()
      return redirect('dhome')
  else:
    # If no existing data found, create an empty form
    form = clinical_summary_form(instance=summary_data)
   
  age=patient.age
  gender=patient.gender
  weight=patient.weight
  ad_date=patient.admission_date
  ad_time=patient.admission_date
  address=patient.address
  phone=patient.phone
  context={'form': form,
       'dname': dname,
       'patient_id':patient_id,
       'name':patient_name,
       'age':age,
       'gender':gender,
       'weight':weight,
       'admission_date':ad_date,
       'time':ad_time,
       'address':address,
       'phone':phone

 }


  return render(request, 'clinical_summary.html', context)




def general_examination(request):
    demail = request.session.get('demail')
    patient_id = request.session.get('current_patient_id')
    

    # Retrieve existing clinical summary data for the patient
    try:
        summary_data = general_examination_data.objects.get(patient_id=patient_id)
    except general_examination_data.DoesNotExist:
        summary_data = None

    doctor = Doctors.objects.get(email=demail)
    dname = doctor.name

    if request.method == "POST":
        # Handle form submission to update or create clinical summary data
        form = general_examination_form(request.POST, instance=summary_data)
        if form.is_valid():
            form.save()
            return redirect('dhome')  # Redirect to home page after saving
    else:
        # If no existing data found, create an empty form
        form = general_examination_form(instance=summary_data)
    patient=Patient.objects.get(patient_id=patient_id)
    patient_name=patient.name
    age=patient.age
    gender=patient.gender
    weight=patient.weight
    ad_date=patient.admission_date
    ad_time=patient.admission_date
    address=patient.address
    phone=patient.phone
    context={'form': form,
             'dname': dname,
             'patient_id':patient_id,
             'name':patient_name,
             'age':age,
             'gender':gender,
             'weight':weight,
             'admission_date':ad_date,
             'time':ad_time,
             'address':address,
             'phone':phone

 }
    

    return render(request, 'general_examination.html', context)



def diagnosis(request):
    demail = request.session.get('demail')
    patient_id = request.session.get('current_patient_id')
   

    # Retrieve existing clinical summary data for the patient
    try:
        summary_data = diagnosis_data.objects.get(patient_id=patient_id)
    except diagnosis_data.DoesNotExist:
        summary_data = None

    doctor = Doctors.objects.get(email=demail)
    dname = doctor.name

    if request.method == "POST":
        # Handle form submission to update or create clinical summary data
        form = diagnosis_form(request.POST, instance=summary_data)
        if form.is_valid():
            form.save()
            return redirect('dhome')  # Redirect to home page after saving
    else:
        # If no existing data found, create an empty form
        form = diagnosis_form(instance=summary_data)
    patient=Patient.objects.get(patient_id=patient_id)
    patient_name=patient.name
    age=patient.age
    gender=patient.gender
    weight=patient.weight
    ad_date=patient.admission_date
    ad_time=patient.admission_date
    address=patient.address
    phone=patient.phone
    context={'form': form,
             'dname': dname,
             'patient_id':patient_id,
             'name':patient_name,
             'age':age,
             'gender':gender,
             'weight':weight,
             'admission_date':ad_date,
             'time':ad_time,
             'address':address,
             'phone':phone

 }

    return render(request, 'diagnosis.html', context)




def previous_investigation(request):
    demail = request.session.get('demail')
    patient_id = request.session.get('current_patient_id')
    

    # Retrieve existing clinical summary data for the patient
    try:
        summary_data = previous_investigation_data.objects.get(patient_id=patient_id)
    except previous_investigation_data.DoesNotExist:
        summary_data = None

    doctor = Doctors.objects.get(email=demail)
    dname = doctor.name

    if request.method == "POST":
        # Handle form submission to update or create clinical summary data
        form = previous_investigation_form(request.POST, instance=summary_data)
        if form.is_valid():
            form.save()
            return redirect('dhome')  # Redirect to home page after saving
    else:
        # If no existing data found, create an empty form
        form = previous_investigation_form(instance=summary_data)
    patient=Patient.objects.get(patient_id=patient_id)
    patient_name=patient.name
    age=patient.age
    gender=patient.gender
    weight=patient.weight
    ad_date=patient.admission_date
    ad_time=patient.admission_date
    address=patient.address
    phone=patient.phone
    context={'form': form,
             'dname': dname,
             'patient_id':patient_id,
             'name':patient_name,
             'age':age,
             'gender':gender,
             'weight':weight,
             'admission_date':ad_date,
             'time':ad_time,
             'address':address,
             'phone':phone

 }

    return render(request, 'previous_investigation.html', context)



def treatment_in_hospital(request):
    demail = request.session.get('demail')
    patient_id = request.session.get('current_patient_id')
    

    # Retrieve existing clinical summary data for the patient
    try:
        summary_data = treatment_in_hospital_data.objects.get(patient_id=patient_id)
    except treatment_in_hospital_data.DoesNotExist:
        summary_data = None

    doctor = Doctors.objects.get(email=demail)
    dname = doctor.name

    if request.method == "POST":
        # Handle form submission to update or create clinical summary data
        form = treatment_in_hospital_form(request.POST, instance=summary_data)
        if form.is_valid():
            form.save()
            return redirect('dhome')  # Redirect to home page after saving
    else:
        # If no existing data found, create an empty form
        form = treatment_in_hospital_form(instance=summary_data)
    patient=Patient.objects.get(patient_id=patient_id)
    patient_name=patient.name
    age=patient.age
    gender=patient.gender
    weight=patient.weight
    ad_date=patient.admission_date
    ad_time=patient.admission_date
    address=patient.address
    phone=patient.phone
    context={'form': form,
             'dname': dname,
             'patient_id':patient_id,
             'name':patient_name,
             'age':age,
             'gender':gender,
             'weight':weight,
             'admission_date':ad_date,
             'time':ad_time,
             'address':address,
             'phone':phone

 }

    return render(request, 'treatment_in_hospital.html', context)


def clinical_progress(request):
    demail = request.session.get('demail')
    patient_id = request.session.get('current_patient_id')
    
    
    

    # Retrieve existing clinical summary data for the patient
    try:
        summary_data = clinical_progress_data.objects.get(patient_id=patient_id)
    except clinical_progress_data.DoesNotExist:
        summary_data = None

    doctor = Doctors.objects.get(email=demail)
    dname = doctor.name

    if request.method == "POST":
        # Handle form submission to update or create clinical summary data
        form = clinical_progress_form(request.POST, instance=summary_data)
        if form.is_valid():
            form.save()
            return redirect('dhome')  # Redirect to home page after saving
    else:
        # If no existing data found, create an empty form
        form = clinical_progress_form(instance=summary_data)
    patient=Patient.objects.get(patient_id=patient_id)
    patient_name=patient.name
    age=patient.age
    gender=patient.gender
    weight=patient.weight
    ad_date=patient.admission_date
    ad_time=patient.admission_date
    address=patient.address
    phone=patient.phone
    context={'form': form,
             'dname': dname,
             'patient_id':patient_id,
             'name':patient_name,
             'age':age,
             'gender':gender,
             'weight':weight,
             'admission_date':ad_date,
             'time':ad_time,
             'address':address,
             'phone':phone

 }
   
    return render(request, 'clinical_progress.html',context)

from django.http import JsonResponse
from django.shortcuts import render
from .models import Doctors, Patient

def all_patients(request):
    demail = request.session.get('demail')
    try:
        doctor = Doctors.objects.get(email=demail)
        dname = doctor.name
    except Doctors.DoesNotExist:
        return JsonResponse({'error': 'Doctor not found'}, status=404)
    
    if request.method == 'GET':
        return render(request, 'all_patients.html', {'dname': dname})
    
    elif request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        if start_date and end_date:
            try:
                patient_details = Patient.objects.filter(admission_date__range=[start_date, end_date])
                if patient_details:
                    results_list = [{'patient_id': patient.patient_id,
                                     'name': patient.name,
                                     'age': patient.age,
                                     'admission_date': patient.admission_date,
                                     'time': patient.time,
                                     'phone': patient.phone,
                                     'address': patient.address} for patient in patient_details]
                    return JsonResponse({'results_list': results_list}, safe=False)
                else:
                    return JsonResponse({'results_list': []}, safe=False)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Invalid request. Please provide start_date and end_date as form parameters.'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



def print_data(request):
    patient_id = request.session.get('current_patient_id')
    demail = request.session.get('demail')
    doctor = Doctors.objects.get(email=demail)
    dname = doctor.name
    patient=Patient.objects.get(patient_id=patient_id)
    patient_name=patient.name
    age=patient.age
    gender=patient.gender
    weight=patient.weight
    ad_date=patient.admission_date
    ad_time=patient.admission_date
    address=patient.address
    phone=patient.phone
    clinicalsummarydata = clinical_summary_data.objects.filter(patient_id=patient_id)
    generalexaminationdata = general_examination_data.objects.filter(patient_id=patient_id)
    diagnosisdata = diagnosis_data.objects.filter(patient_id=patient_id)
    previousinvestigationdata = previous_investigation_data.objects.filter(patient_id=patient_id)
    treatmentinhospitaldata = treatment_in_hospital_data.objects.filter(patient_id=patient_id)
    clinicalprogressdata = clinical_progress_data.objects.filter(patient_id=patient_id)
    prescription=Prescription.objects.filter(patient_id=patient_id)
    

    
    context = {
        'clinical_summary_data': clinicalsummarydata,
        'general_examination_data': generalexaminationdata,
        'diagnosis_data':diagnosisdata,
        'previous_investigation_data':previousinvestigationdata,
        'treatment_in_hospital_data':treatmentinhospitaldata,
        'clinical_progress_data':clinicalprogressdata,
        'dname': dname,
        'prescription':prescription,
             'patient_id':patient_id,
             'name':patient_name,
             'age':age,
             'gender':gender,
             'weight':weight,
             'admission_date':ad_date,
             'time':ad_time,
             'address':address,
             'phone':phone

    }
    return render(request, 'print_data.html', context)



def search_tablets(request):
    query = request.GET.get('query', '')
    print("tablet=",query)
    # Perform a live search for tablets based on the query
    tablets = Tablet.objects.filter(name__icontains=query) 
    print(tablets)
    
    results_tab = [{'name': tablet.name} for tablet in tablets]

    return JsonResponse({'results_tab': results_tab})



def prescription(request):
    # Render the prescription form template
    return render(request, 'prescription.html')



def save_prescription(request):
    if request.method == 'POST':
        prescription_data_json = request.POST.get('prescription_data') # Retrieve JSON data from POST
        prescription_data = json.loads(prescription_data_json) # Deserialize JSON data
        patient_id = request.session.get('current_patient_id')
        patient=Patient.objects.get(patient_id=patient_id)
        patient_name=patient.name
        
        for item in prescription_data:
            tablet_name = item['tabletName']
            morning = item['morning']
            afternoon = item['afternoon']
            evening = item['evening']
            
            
            # Create Prescription object and save it to the database
            prescription = Prescription.objects.create(
                patient_id=patient_id,
                patient_name=patient_name,
                tablet=tablet_name,
                morning=morning,
                afternoon=afternoon,
                evening=evening
            )
            # You can perform additional processing or validations here if needed
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    



'''def tablet(request):
    


# Iterate over the list and create Tablet objects
    for name in tablet_list:
        tablet = Tablet(name=name)
        tablet.save()

    return HttpResponse("data saved success")'''