from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserPersonalizadoAdmin(UserAdmin):
    list_display = ('fullname', 'email_academico', 'phone', )
    search_fields = ('fullname', 'email_academico', 'phone',)
    list_per_page = 30
    fieldsets = UserAdmin.fieldsets + (('Informações Acadêmicas', {'fields': ('fullname', 'email_academico','phone')}),)
    add_fieldsets = UserAdmin.add_fieldsets + (('Informações Acadêmicas', {'fields': ('fullname', 'email_academico','phone')}),)

