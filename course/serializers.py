from rest_framework import serializers
from .models import Course, Syllabus, Project


class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = ['id', 'title', 'description']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description']


class SimpleCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'career_path'
        ]


class CourseSerializer(serializers.ModelSerializer):
    syllabuses = SyllabusSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'career_path',
            'syllabuses',
            'projects'
        ]
