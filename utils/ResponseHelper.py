from rest_framework.response import Response

def successResponse(data):
    return Response({
        "success": True,
        "errors": None,
        "data": data
    })

def failedResponse(err, status):
    return Response({
        "success": False,
        "errors": err,
        "data": None
    }, status=status)
