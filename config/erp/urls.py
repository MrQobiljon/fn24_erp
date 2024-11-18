from django.urls import path
from .views import StudentApiView, CourseAPIView

urlpatterns = [
    path('students/', StudentApiView.as_view()),
    path('students/<int:pk>/', StudentApiView.as_view(), name='student-detail'),
    path('courses/', CourseAPIView.as_view()),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course-detail'),
]
