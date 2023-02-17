from rest_framework.views import APIView
from rest_framework import status

from .models import Course as CourseModel
from django.db.models import Q
from .serializers import SimpleCourseSerializer, CourseSerializer
from utils.ResponseHelper import successResponse, failedResponse


class Course(APIView):
    def get(self, request, *args, **kwargs):
        try:
            if 'course_id' in list(kwargs):
                course = CourseModel.objects.filter(
                    id=kwargs['course_id']
                ).first()

                if course == None:
                    return failedResponse('Data not found', status.HTTP_404_NOT_FOUND)

                serializer = CourseSerializer(course)
            else:
                search = request.GET.get('q')
                if search == None:
                    courses = CourseModel.objects.all()
                else:
                    courses = CourseModel.objects.filter(
                        Q(title__contains=search)
                        |
                        Q(description__contains=search)
                    )
                serializer = SimpleCourseSerializer(courses, many=True)

            return successResponse(serializer.data)
        except Exception as e:
            return failedResponse(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
