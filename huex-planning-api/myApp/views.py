from django.http import JsonResponse
import json
from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# import the scheduler logic
from .scheduler import Scheduler

@method_decorator(csrf_exempt, name='dispatch')
class AppointmentsView(View):
    def post(self, request):
        """
        Takes information of patients and slots from request
        prepares a plan for appointments scheduled for the day.
        """
        results, msg, code = Scheduler(request.body.decode())
        return JsonResponse({"results": results, "message": msg},  content_type="application/json" , status= code)