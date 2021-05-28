from django.test import TestCase, Client
from django.contrib.auth.models import User
import json

class CentersTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.client = Client()

    def test_get_all_centers(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get('/center/')
        self.assertEquals(response.status_code, 200)

    def test_create_or_update_center(self):
        self.client.login(username=self.user.username, password='12345')
        python_dict = {"cen_location": "bangalore", "cen_slots": 40}
        response = self.client.post('/center/',
                                json.dumps(python_dict),
                                content_type="application/json")
        self.assertEquals(response.status_code, 201)
        # self.assertEquals(response.message, 'Successfully Inserted or Updated a row')