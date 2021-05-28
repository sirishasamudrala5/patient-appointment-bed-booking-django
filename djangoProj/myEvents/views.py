from django.http import HttpResponse
import datetime
import json
from django.views import View


class Index(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the Events App index page .")

class Users(View):
    def get(self, request):
        response = {'uuid': '01'}
        response_json = json.dumps(response)
        return HttpResponse(response_json, content_type="application/json" , status=200)

class UserEvents(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the Events App User events get page .")
    def post(self, request, id):
        return HttpResponse("Hello {}, world. You're at the Events App user events post page .".format(id))

class Reports(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the Events App index page .")