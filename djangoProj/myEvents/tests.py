from django.test import TestCase
# from .views import Users


class UsersTestCase(TestCase):
    def test_get_users(self):
        response = self.client.get('/myEvents/users/')
        self.assertEquals(response.status_code, 200)
