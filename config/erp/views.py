from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

# Create your views here.


class StudentApiView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                student = Student.objects.get(pk=pk)
                return Response(StudentSerializer(student).data)
            except:
                return Response({"message": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)

        students = Student.objects.all()
        return Response(StudentSerializer(students, many=True).data)

    def post(self, request: Request, pk=None):
        if pk:
            return Response("Method POST not allowed", status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response(StudentSerializer(student).data)

    def put(self, request: Request, pk=None):
        if not pk:
            return Response("Method PUT not allowed", status=status.HTTP_404_NOT_FOUND)

        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_student = serializer.update(student, serializer.validated_data)

            return Response(StudentSerializer(updated_student).data)
        except:
            return Response({"message": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        pass
