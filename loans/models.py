from django.db import models
from django.utils import timezone

class Loans(models.Model):
    aluno = models.ForeignKey("accounts.User", on_delete=models.CASCADE, verbose_name="Aluno" )
    notebook = models.ForeignKey("inventory.Notebook", on_delete=models.CASCADE, verbose_name="Notebook")
    carregador = models.BooleanField(default=False)
    data_retirada = models.DateTimeField(auto_now_add=True, verbose_name="Data de Retirada")
    data_devolucao= models.DateTimeField(null=True,blank=True, verbose_name="Data de Devolução")

    def __str__(self):
        return f"{self.aluno}-{self.notebook}"
    
    class Meta:
        verbose_name = 'Empréstimo'

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.data_devolucao:
            self.notebook.status = 'EMPRESTADO'
        else:
            self.notebook.status = 'DISPONIVEL'
        self.notebook.save()
        super().save(*args, **kwargs)
        


        
    
