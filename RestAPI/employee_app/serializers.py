from rest_framework import serializers

# from Employee_Details.employee_app.models import Employee, Salary
from .models import Employee, Salary


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'
