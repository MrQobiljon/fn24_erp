from django.urls import path
from .views import StudentApiView

urlpatterns = [
    path('students/', StudentApiView.as_view()),
    path('students/<int:pk>/', StudentApiView.as_view()),
]
