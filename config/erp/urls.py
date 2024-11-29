from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentApiViewSet, CourseAPIView, SendEmailAPIView


router = DefaultRouter()
router.register('students', StudentApiViewSet, basename='student')
print(router.urls)


urlpatterns = [
    path('courses/', CourseAPIView.as_view()),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course-detail'),

    path('send-email/', SendEmailAPIView.as_view()),

    path('', include(router.urls)),
]

