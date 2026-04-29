from rest_framework.test import APITestCase,APIClient
from django.urls import reverse

class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        user_data = {
            'email':"email@gmail.com",
            'username': 'email',
            'password': ''
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()