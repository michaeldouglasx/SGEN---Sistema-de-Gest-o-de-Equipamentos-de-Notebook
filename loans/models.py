from django.db import models
from django.utils import timezone

class Loans(models.Model):
    aluno = models.ForeignKey("accounts.User", on_delete=models.CASCADE, verbose_name="Aluno" )
    notebook = models.ForeignKey("inventory.Notebook", on_delete=models.CASCADE, verbose_name="Notebook")
    carregador = models.BooleanField(default=False)
    data_saida = models.DateTimeField(auto_now_add=True, verbose_name="Data de Saída")
    data_devolucao= models.DateTimeField(null=True,blank=True, verbose_name="Data de devolução")

    def __str__(self):
        return f"{self.aluno}-{self.notebook}"
    
