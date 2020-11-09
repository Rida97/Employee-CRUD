from django.urls import path

from .views import api_detail_employee_view

urlpatterns = [
    path('employees/', api_detail_employee_view)
]

