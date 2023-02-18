from django.test import TestCase, Client
from django.urls import reverse
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('exercise')

    def test_exercise_python(self):
        payload = {
            "language": "python",
            "code": "print('Hello World')"
        }
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

        data = json.loads(response.content)
        self.assertEqual(data['success'], True)
        self.assertIn('Hello World', data['data'])

    def test_exercise_javascript(self):
        payload = {
            "language": "javascript",
            "code": "console.log('Hello Salim')"
        }
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

        data = json.loads(response.content)
        self.assertEqual(data['success'], True)
        self.assertIn('Hello Salim', data['data'])
