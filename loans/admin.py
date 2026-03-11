from django.contrib import admin
from .models import Loans

@admin.register(Loans)
class LoansAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'notebook', 'data_retirada', 'data_devolucao', 'carregador',)
    search_fields = ('aluno__fullname', 'notebook__numero_patrimonio',)
    list_per_page = 20
    readonly_fields = ('data_retirada',)
    fields = ('aluno', 'notebook', 'carregador', 'data_retirada', 'data_devolucao')
    list_filter = ('data_retirada', 'carregador')
    date_hierarchy = 'data_retirada'


    