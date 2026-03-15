from django.urls import path
from ..views.LoginView import Login_View
from ..views.CadastroView import Cadastro_View


urlpatterns = [
    path('login/', Login_View, name='login'),
    path('cadastro', Cadastro_View, name='cadastro')
]
