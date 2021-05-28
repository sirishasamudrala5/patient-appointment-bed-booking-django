from django.test import TestCase,Client
from django.contrib.auth.models import User
import json

class PatientsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.client = Client()

    def test_get_all_patients(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get('/patient/')
        self.assertEquals(response.status_code, 200)

    def test_create_or_update_patient(self):
        self.client.login(username=self.user.username, password='12345')
        python_dict = {"pat_name": "pradeep", "age": 35, "flag": True, "last_dialysis": "2019-06-01T18:30:00Z", "next_dialysis": "2019-08-01T18:30:00Z", "start_dialysis": "2019-06-01T18:30:00Z", "end_dialysis": "2020-06-01T18:30:00Z", "freq_dialysis": 2, "pref_days": '1,4', "pref_time": '1,2', "duration": 3, "registered_date": "2019-06-01T18:30:00Z", "medical_cond": '1,2,3'}
        response = self.client.post('/patient/',
                                json.dumps(python_dict),
                                content_type="application/json")
        self.assertEquals(response.status_code, 201)
        # self.assertEqual(response.json()['name'], '<name>')
        # self.assertEquals(response.message, 'Successfully Inserted or Updated a row')