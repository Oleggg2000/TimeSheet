from django.shortcuts import render
from django.http import HttpResponse

from .models import Records, Customer

def test_stub(request):
    return HttpResponse('Yeh, boy! Test stub is working!!')

def test_django(request):
    data = {'title': 'My First view/controller!', 'records': Records.objects.all(), 'img': Customer.objects.first()}
    return render(request, 'test_django/index.html', data)
