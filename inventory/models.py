from django.db import models
MARCAS = [ ("Acer", "Acer"), ("DELL", "Dell"),("APPLE","Apple"), ("VAIO", "Vaio"), ("AVELL","Avell"), ("ALIENWARE","Alienware"), ("Samsung","Samsung"), ("HP","HP"), ("ASUS","Asus") ]

CORES = [
    ("PRETO", "Preto"), ("CINZA", "Cinza"), 
    ("BRANCO", "Branco"), ("PRATA", "Prata")
]

STATUS = [
    ("DISPONIVEL", "Disponível"),
    ("MANUTENCAO", "Manutenção"),
    ("EMPRESTADO", "Emprestado"),
]

class Notebook(models.Model):
    numero_patrimonio = models.CharField(blank=False, max_length=6, unique=True, verbose_name="Nº Patrimônio")
    marca= models.CharField(max_length=20, choices=MARCAS)
    cor = models.CharField(max_length=30,  choices=CORES)
    modelo = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices=STATUS, default="DISPONIVEL")

    def __str__(self):
        return f"{self.numero_patrimonio} - {self.marca}"
