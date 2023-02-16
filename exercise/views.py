from rest_framework.views import APIView
from rest_framework.response import Response
import subprocess


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

        # Check if there was an error
        if result.returncode != 0:
            return Response({
                'status': 'error',
                'output': result.stderr
            })
        else:
            return Response({
                'status': 'success',
                'output': result.stdout
            })
