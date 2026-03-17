from django.shortcuts import redirect
from django.contrib.auth import logout

def Logout_View(request):
    logout(request)
    return redirect("login")