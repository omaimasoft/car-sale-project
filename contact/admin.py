from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'telephone', 'date_envoi')
    search_fields = ('nom_complet', 'telephone')
    list_filter = ('date_envoi',)
    readonly_fields = ('date_envoi',)
