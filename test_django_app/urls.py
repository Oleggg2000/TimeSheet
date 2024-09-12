from django.urls import path, include
from . import views

app_name = 'test_app'

urlpatterns = [
    path("main/", views.test_django, name='test_main'),
    path("stub/", views.test_stub, name='test_stub'),
]

