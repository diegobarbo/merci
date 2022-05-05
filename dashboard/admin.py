from django.contrib import admin
from .models import Peca, Venda
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'Merci Administração'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'categoria')
    list_filter = ['categoria']


admin.site.register(Peca, ProductAdmin)
admin.site.register(Venda)
admin.site.unregister(Group)
