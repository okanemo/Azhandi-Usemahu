from django.shortcuts import render
from django.http import HttpResponse

from .models import PatientLab, LabStudies

from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@csrf_exempt
def addPatiens(request):
    if request.method == "POST":
        payloads = json.loads(request.body)
        try:
            if 'patient_data' in payloads:
                response = patientDataCheck(payloads)
            else:
                response = patientData(payloads)
            # print(PatientLab.objects.get(patient_name=))
        except:
            response = json.dumps([{'Error': 'Patient data cannot be added'}])
        return HttpResponse(response, content_type='text/json')
    else:
        response = json.dumps([{'Error': 'No data recieved'}])
        return HttpResponse(response, content_type='text/json')


def patientDataCheck(payloads):
    pd = payloads['patient_data']
    id_number = pd['id_number']
    patient_name = f"{pd['first_name']} {pd['last_name']}"
    mobile_phone = pd['phone_mobile']
    gender = pd['gender']
    date_of_birth = pd['date_of_birth']
    lab_number = payloads['lab_number']
    clinic_code = payloads['clinic_code']
    date_of_test = payloads['date_of_test']
    print('aaaa')
    if PatientLab.objects.filter(patient_name=patient_name).count() > 0:
        return json.dumps([{'Error': 'Patient data Already Exist'}])
    pl = PatientLab(id_number=id_number, patient_name=patient_name, gender=gender, date_of_birth=date_of_birth,
                    lab_number=lab_number, clinic_code=clinic_code, date_of_test=date_of_test, mobile_phone=mobile_phone)
    pl.save()
    labStudies(payloads)

    return json.dumps([{'Success': 'Patient data added'}])


def patientData(payloads):
    id_number = payloads['id_number']
    patient_name = payloads['patient_name']
    gender = payloads['gender']
    date_of_birth = payloads['date_of_birth']
    lab_number = payloads['lab_number']
    clinic_code = payloads['clinic_code']
    date_of_test = payloads['date_of_test']
    print()
    if PatientLab.objects.filter(patient_name=patient_name).count() > 0:
        return json.dumps([{'Error': 'Patient data Already Exist'}])

    pl = PatientLab(id_number=id_number, patient_name=patient_name, gender=gender, date_of_birth=date_of_birth,
                    lab_number=lab_number, clinic_code=clinic_code, date_of_test=date_of_test, mobile_phone='-')
    pl.save()
    labStudies(payloads)

    return json.dumps([{'Success': 'Patient data added'}])


def labStudies(payloads):
    labDataCheck = len(payloads['lab_studies'])
    lab_studies = payloads['lab_studies']
    if labDataCheck:
        for item in lab_studies:
            code = item['code']
            name = item['name']
            value = item['value']
            unit = item['unit']
            ref_range = item['ref_range']
            finding = item['finding']
            result_state = item['result_state']
            ls = LabStudies(code=code, name=name, value=value, unit=unit,
                            ref_range=ref_range, finding=finding, result_state=result_state)
            ls.save()
