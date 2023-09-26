from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('employee-add', EmployeeAdd.as_view(),name='employee-add'),
    path('employee-detail/<int:id>/', EmployeeDetail.as_view(),name='employee-detail'),
    path('employee-update/<int:id>/', EmployeeUpdate.as_view(),name='employee-update'),
    path('employee-delete/<int:id>/', EmployeeDelete.as_view(),name='employee-delete'),


]
