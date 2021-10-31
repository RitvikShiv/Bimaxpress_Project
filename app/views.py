from rest_framework.views import APIView

from .models import Demo
from .serializers import DemoSerializers
from django.http.response import JsonResponse


class Data(APIView):   
    
    def get(self, request):
        user =Demo.objects.all()
        serializer = DemoSerializers(user, many=True)
        return JsonResponse(serializer.data,safe=False)
        
    def post(self, request, format=None):
        data = request.data
        serializer = DemoSerializers(data=data)
        if serializer.is_valid():
            poll = Users(**data)
            poll.save()
            response = serializer.data
            return JsonResponse("Added Successfully",safe=False)

    def put(self, request, format=None):
        data=request.data
        user=Demo.objects.get(UserId=data['UserId'])
        serializer=DemoSerializers(user,data=data)
        if serializer.is_valid():
            poll = Users(**data)
            serializer.save()
            response = serializer.data
            return JsonResponse("Updated Successfully",safe=False)
    
    
    def delete(self, id=0):
        print(id);
        user=Demo.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Deleted Successfully",safe=False)

