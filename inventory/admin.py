from django.contrib import admin
from .models import Notebook, Brand

@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):

    list_display = ('numero_patrimonio', 'marca',  'modelo', 'status', 'cor', )
    list_filter = ('numero_patrimonio', 'status')
    search_fields = ('numero_patrimonio',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)
    search_fields = ('brand',)
    list_filter = ('brand',)
    
    
