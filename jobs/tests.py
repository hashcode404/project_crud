from django.test import TestCase

# jobs/tests.py
from rest_framework.test import APITestCase
from rest_framework import status

class JobTests(APITestCase):
    def test_create_job(self):
        url = '/api/jobs/'
        data = {
            "title": "Software Engineer",
            "description": "Develop software.",
            "company": {"name": "Tech Corp", "location": "New York"},
            "location": "New York",
            "salary": 80000
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
