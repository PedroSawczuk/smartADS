from django.contrib import admin
from .models import Meta

class MetaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tempo', 'email', 'criado_em')
    search_fields = ('nome', 'email')
    list_filter = ('tempo',)
    list_editable = ('tempo',)
    ordering = ('-criado_em',)

admin.site.register(Meta, MetaAdmin)
