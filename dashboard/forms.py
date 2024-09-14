from django import forms
from . models import Product, Client, Fournisseur, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantite','designation', 'prix', 'fournisseur', 'date_peremption']

        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'adresse', 'phone']


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['name', 'email', 'adresse', 'phone']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'client', 'quantite', 'date']

        
# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = ['product', 'client', 'quantite', 'date']