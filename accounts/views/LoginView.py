from django.http import HttpResponse
from django.shortcuts import render

def Login_View(request):
    return render(request, template_name='login.html')