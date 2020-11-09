from datetime import datetime

from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET'])
def api_detail_employee_view(request):
    if request.method == 'GET':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
