from django.contrib import admin
from .models import Client
# Register your models here.

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone_number', 'email', 'reason', 'description', 'submitted_at')
#     search_fields = ('name', 'email', 'reason')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('userId', 'name', 'email', 'phone', 'user_role', 'country', 'company', 'designation' )
    search_fields = ('name', 'email', 'userId', 'phone', 'company')