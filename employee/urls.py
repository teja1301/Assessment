from django.urls import path
from .views import create_employee, update_employee, delete_employee, get_employee

urlpatterns = [
    path('create_employee/', create_employee, name='create_employee'),
    path('update_employee/<str:regid>/', update_employee, name='update_employee'),
    path('delete_employee/<str:regid>/', delete_employee, name='delete_employee'),
    path('get_employee/', get_employee, name='get_employee'),
]
