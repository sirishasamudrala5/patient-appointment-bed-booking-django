from django.http import HttpResponse, JsonResponse
import json
from django.views import View
from centers.models import Centers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class CentersView(View):
    def get(self, request):
        """
        fetch all dialysis centers if no id is passed
        or 
        fetch a diaysis center based on id
        """
        cen_id = request.GET.get('id', None)
        if(cen_id):
            results, msg, code = Centers.objects.get_center(cen_id)
            results = list(results.values())
        else:
            results, msg, code = Centers.objects.get_all_centers()
            results = list(results.values())
        return JsonResponse({"results": results, "message": msg},  content_type="application/json" , status= code)

    def post(self, request):
        """
        create a dialysis center if no id is passed
        or 
        update the dialysis center based on id
        """
        results, msg, code = Centers.objects.create_or_update_center(request.body.decode())
        return JsonResponse({"results": results, "message": msg},  content_type="application/json" , status= code)