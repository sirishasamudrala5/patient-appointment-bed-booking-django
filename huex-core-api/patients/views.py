from django.http import HttpResponse, JsonResponse
import json
from django.views import View
from patients.models import Patients
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class PatientsView(View):
    def get(self, request):
        """
        fetch all patients list if no id is passed
        or 
        fetch a patient based on id
        """
        pat_id = request.GET.get('id', None)
        if(pat_id):
            results, msg, code = Patients.objects.get_patient(pat_id)
            results = list(results.values())
        else:
            results, msg, code = Patients.objects.get_all_patients()
            results = list(results.values())
        return JsonResponse({"results": results},  content_type="application/json" , status= 200)

    def post(self, request):
        """
        create a patient if no id is passed
        or 
        update the patient details based on id
        """
        results, msg, code = Patients.objects.create_or_update_patient(request.body.decode())
        return JsonResponse({"results": results, "message": msg},  content_type="application/json" , status= code)
