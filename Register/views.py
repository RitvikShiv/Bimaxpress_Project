



from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from Register.models import Register
from Register.serializers import  RegisterSerializer

# Create your views here.


@api_view(['GET', 'POST' , 'PUT', 'DELETE'])
def Data(request, id=0):
    if request.method == 'GET':
        Register = Register.objects.all()
        RegisterSerializer = RegisterSerializer(Register, many=True)
        return JsonResponse(RegisterSerializer.data, safe=False)

    elif request.method == 'POST':
        


        data = request.data
        RegisterSerializer = bimaxpressSerializer(data=data)
        if RegisterSerializer.is_valid():
            RegisterSerializer = Users(**data)
            RegisterSerializer.save()
            response = RegisterSerializer.data
            return JsonResponse("Added Successfully",safe=False)

    elif request.method == 'PUT':
      

        data=request.data
        Register=Register.objects.get(S_No=data['S_No'])
        RegisterSerializer=RegisterSerializer(Register,data=data)
        if RegisterSerializer.is_valid():
            bimaxpress_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)

    elif request.method == 'DELETE':
        Register=Register.objects.get(S_No=request.data["S_No"])
        Register.delete()
        return JsonResponse("The record has been deleted successfully!")







