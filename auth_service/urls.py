from django.urls import path
from . import views
from pathlib import Path

app_name = Path.cwd().as_posix()

urlpatterns = [
    path('sign-in/', views.sign_in_view, name='login'),
    path('sign-up/', views.registration_view, name='register'),
]
