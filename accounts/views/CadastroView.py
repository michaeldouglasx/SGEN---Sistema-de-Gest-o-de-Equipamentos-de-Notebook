from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import CadastroForm

def Cadastro_View(request):
    if request.method == 'POST':
        formulario = CadastroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
        
    else:
        formulario = CadastroForm()
    
    return render(request, 'cadastro.html', {"formulario": formulario})