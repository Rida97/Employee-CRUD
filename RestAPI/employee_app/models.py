import uuid
from django.db import models


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Salary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salary = models.IntegerField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return "%s Displaying the salary : " % self.salary

#   e = Employee("Rida Fatima", 2)
#   s = Salary(55000, employee=e)
#   s.employee
#   s.employee.id
