from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import authentication

from rest_framework import mixins

from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
from .permissions import StudentPermission

# Create your views here.


class StudentApiView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class StudentDetailApiView(GenericAPIView,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'student_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

















# class StudentApiView(GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request: Request):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request: Request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         student = serializer.save()
#         return Response(serializer.data)
#
#
# class StudentDetailApiView(GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_url_kwarg = 'student_id'
#
#     def get(self, request: Request, student_id: int):
#         print(self.kwargs)
#         student = self.get_object()
#         serialzier = self.get_serializer(student)
#         return Response(serialzier.data)









# class StudentApiView(APIView):
#     serializer = StudentSerializer
#     queryset = Student.objects.all()
#     permission_classes = [permissions.IsAuthenticated]
#     # authentication_classes = [authentication.TokenAuthentication]
#
#     def check_obj(self, request, obj):
#         try:
#             self.check_object_permissions(request, obj)
#             return True
#         except:
#             return False
#
#     def get_perms_students(self):
#         list_students = []
#         students = Student.objects.all()
#         for student in students:
#             try:
#                 self.check_object_permissions(self.request, student)
#                 list_students.append(student)
#             except:
#                 pass
#         return list_students
#
#     def get(self, request: Request, pk=None):
#
#         if pk:
#             try:
#                 student = Student.objects.get(pk=pk)
#                 if self.check_obj(request, student):
#                     return Response(self.serializer(student, context={"request": request}).data)
#                 else:
#                     return Response({"message": "Student Not Permission"}, status=status.HTTP_404_NOT_FOUND)
#             except:
#                 return Response({"message": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)
#         return Response(self.serializer(self.get_perms_students(), context={"request": request}, many=True).data)
#
#     def post(self, request: Request, pk=None):
#         if pk:
#             return Response("Method POST not allowed", status=status.HTTP_404_NOT_FOUND)
#         serializer = self.serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         student = serializer.save()
#         return Response(StudentSerializer(student).data)
#
#     def put(self, request: Request, pk=None):
#         if not pk:
#             return Response("Method PUT not allowed", status=status.HTTP_404_NOT_FOUND)
#
#         try:
#             student = Student.objects.get(pk=pk)
#             serializer = self.serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             updated_student = serializer.update(student, serializer.validated_data)
#
#             return Response(self.serializer(updated_student).data)
#         except:
#             return Response({"message": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, pk=None):
#         if not pk:
#             return Response("Method DELETE not allowed", status=status.HTTP_404_NOT_FOUND)
#
#         try:
#             student = Student.objects.get(pk=pk)
#             student.delete()
#             return Response({"message": "success"})
#         except:
#             return Response({"message": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND)


class CourseAPIView(APIView):
    courses = Course.objects.all()
    serializer = CourseSerializer
    def get(self, request: Request, pk=None):
        if pk:
            try:
                student = self.courses.get(pk=pk)
                return Response(self.serializer(student, context={"request": request}).data)
            except:
                return Response({"message": "Course Not Found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(self.serializer(self.courses, context={"request": request}, many=True).data)
