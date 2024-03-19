from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data, Services
from .serializer import DataSerializer,ServicesSerializer

# Create your views here.
@api_view(['GET'])
def getData(request):
    app=Data.objects.all()
    serializer=DataSerializer(app,many=True)
    return Response(serializer.data)
# def getData(request):
#     serv=Services.objects.all()
#     serializer1=ServicesSerializer(serv,many=True)
    
#     return Response(serializer1.data)

@api_view(['POST'])
def postData(request):
    serializer=DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    