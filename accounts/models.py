from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True, null=False)
    fullname = models.CharField(max_length=150, blank=True, verbose_name="Nome Completo")
    email_pessoal = models.EmailField(max_length=150, blank=True)
    email_academico = models.EmailField( max_length=150, blank=False, verbose_name="E-mail Acadêmico", help_text="Example: aluno@edu.df.senac.br")
    phone = models.CharField(blank=False, max_length= 15, help_text="Formato (61) 9 9888-7777", verbose_name="Telefone de contato" )

    
    def __str__(self):
        return self.fullname