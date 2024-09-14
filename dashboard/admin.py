from django.contrib import admin
from . models import Product, Order, Client, Fournisseur
from django.contrib.auth.models import Group

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantite', 'designation', 'prix', 'fournisseur', 'date_peremption')
    list_filter = ('category',)

admin.site.site_header = 'AGS'
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Fournisseur)
# admin.site.unregister(Group)
