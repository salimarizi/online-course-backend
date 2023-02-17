from rest_framework.views import APIView
from rest_framework import status
import subprocess

from utils.ResponseHelper import successResponse, failedResponse


class Exercise(APIView):
    def post(self, request, *args, **kwargs):
        language = request.data.get('language')
        
        if language == 'javascript':
            filename = 'script.js'
            command = ['node']
        if language == 'python':
            filename = 'script.py'
            command = ['python3']
        
        with open(filename, 'w') as file:
            file.write(request.data.get('code'))
        
        command.append(filename)

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check if there is an error
        if result.returncode != 0:
            return failedResponse(result.stderr, status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return successResponse(result.stdout)
