from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response
from app.serializers import *

class ProductCurd(APIView):
    def get(self,request):
        PDO=Product.objects.all()
        PJO=ProductModelSerializers(PDO,many=True)
        return Response(PJO.data)
    
    def post(self,request):
        JDO=request.data
        PDO=ProductModelSerializers(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'insert':'Data is inserted successfull'})
        else:
            return Response({'error':'insertion of data is error'})