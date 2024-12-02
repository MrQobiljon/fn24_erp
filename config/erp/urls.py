from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentApiViewSet, CourseAPIView, SendEmailAPIView, VideoApiViewSet


router = DefaultRouter()
router.register('students', StudentApiViewSet, basename='student')
router.register('videos', VideoApiViewSet, basename='videos')


urlpatterns = [
    path('courses/', CourseAPIView.as_view()),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course-detail'),

    path('send-email/', SendEmailAPIView.as_view()),

    path('', include(router.urls)),
]

