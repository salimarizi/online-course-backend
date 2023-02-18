from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import Course, Syllabus, Project


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        course = Course.objects.create(
            title='Course 1',
            description='Description',
            career_path='Careers'
        )

        Syllabus.objects.bulk_create([
            Syllabus(course=course, title='Syllabus 1',
                     description='Description'),
            Syllabus(course=course, title='Syllabus 2'),
        ])

        Project.objects.bulk_create([
            Project(course=course, title='Project 1',
                    description='Description'),
            Project(course=course, title='Project 2'),
        ])

        self.url = reverse('courses')
        self.urlDetail = reverse(
            'course',
            kwargs={'course_id': course.id}
        )

    def test_course_lists(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

        data = json.loads(response.content)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['data']), 1)
        self.assertEqual(data['data'][0]['title'], 'Course 1')

    def test_course_detail(self):
        response = self.client.get(self.urlDetail)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        
        data = json.loads(response.content)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['data']['syllabuses']), 2)
        self.assertEqual(len(data['data']['projects']), 2)
