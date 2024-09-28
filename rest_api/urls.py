from rest_framework.authtoken import views
from django.urls import path
from pathlib import Path
import os
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = Path.cwd().as_posix()

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='get_token'),
    # path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),

    path('token/', views.rest_sign_in, name='get_token'),
    path('token/refresh/', views.rest_sign_in, name='refresh_token'),

    path('records/', views.records_view, name='records_view'),
]
