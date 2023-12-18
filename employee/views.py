from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['POST'])
def create_employee(request):
    try:
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee created successfully", "regid": serializer.data["id"], "success": True}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message": "Employee creation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_employee(request, regid):
    try:
        employee = get_object_or_404(Employee, id=regid)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee details updated successfully", "success": True}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message": "Employee updation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_employee(request, regid):
    try:
        employee = get_object_or_404(Employee, id=regid)
        employee.delete()
        return Response({"message": "Employee deleted successfully", "success": True}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": "Employee deletion failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_employee(request):
    try:
        regid = request.GET.get('regid', None)
        if regid:
            employee = get_object_or_404(Employee, id=regid)
            serializer = EmployeeSerializer(employee)
            return Response({"message": "Employee details found", "success": True, "employees": [serializer.data]}, status=status.HTTP_200_OK)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            if employees.exists():
                return Response({"message": "Employee details found", "success": True, "employees": serializer.data}, status=status.HTTP_200_OK)
            return Response({"message": "Employee details not found", "success": False, "employees": []}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": "Internal Server Error", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)