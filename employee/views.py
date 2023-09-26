from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializer import *
from django.shortcuts import get_object_or_404
# Create your views here.


class EmployeeDetail(APIView):
    def get(self, request, id=None):
       
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)
        emp = Employee.objects.all()
        serializer=EmployeeSerializer(emp,many=True)
        return Response(serializer.data)


class EmployeeAdd(APIView):

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Employee Successfully Added'},status=status.HTTP_201_CREATED)
        
    
class EmployeeUpdate(APIView):
    def put(self,request,id):
        
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Employee data updated'})
        


    def patch(self, request, id):
        
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Employee partially updated'})
        

class EmployeeDelete(APIView):

    def delete(self, request, id):
        
        emp = get_object_or_404(Employee, id=id)
        emp.delete()
        return Response({'message':'Data Deleted'})

