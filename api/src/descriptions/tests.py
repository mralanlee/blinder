from django.test import TestCase
from rest_framework.test import APIClient
from users.models import User
from django.urls import reverse
from descriptions.models import Description
from rest_framework import status

# Create your tests here.
class TestDescriptions(TestCase):
    username = 'user_test'

    email = 'teste@teste.com'

    password = 'senha123456'

    route = reverse('descriptions.create')

    validated_data = {
        'title': 'Test Description Title',
        'description': 'Bla bla bla bla...',
        'emoji': None
    }

    def setUp(self):
        user_test = User.objects.create_user(self.username,email=self.email,password=self.password)
        self.client = APIClient()
        self.client.force_authenticate(user_test)

    def test_can_create_description(self):
        data = self.validated_data
        response = self.client.post(self.route, data=data, format='json')
        with self.subTest('User must be create description with validated data', response=response):
            #status check
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            #database rows
            db_users = Description.objects.count()
            self.assertEqual(1, db_users)
            #response API
            body = response.json()
            self.assertIn('id',body)
            self.assertIn('title',body)
            self.assertIn('description',body)
            self.assertIn('emoji',body)
