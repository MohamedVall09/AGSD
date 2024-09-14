from django.db import models
from django.utils import timezone   
from django.contrib.auth.models import User 
from django import forms


CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Fournisseur(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    adresse = models.CharField(max_length=50)
    phone = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Fournisseur'
    def __str__(self):
        return '{} by {}'.format(self.name, self.email) 

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantite = models.PositiveIntegerField(null=True)
    designation = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    fournisseur = models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    date_peremption = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Product'  

    def __str__(self):
        return f'{self.name}'

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    adresse = models.CharField(max_length=50)
    phone = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Client'
    def __str__(self):
        return '{} by {}'.format(self.name, self.email) 


# class Transaction(models.Model):
#     Product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     client = models.ForeignKey(Client,on_delete=models.CASCADE)
#     quantite = models.IntegerField(Product,on_delete=models.CASCADE)
#     date = models.DateField(default=timezone.now)

#     class Meta:
#         verbose_name_plural = 'Transaction'
#     def __str__(self):
#         return '{} by {}'.format(self.date, self.quantite)
    


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    client = models.ForeignKey(Client, models.CASCADE, null=True)
    quantite = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Order'
    def __str__(self):
        if self.staff:
           return f'{self.product} ordered by {self.staff.username}'
        return f'{self.product} ordered by [unknown staff]'
    
    def save(self, *args, **kwargs):
        if self.product.quantite >= self.quantite:
            self.product.quantite -= self.quantite
            self.product.save()
            super().save(*args, **kwargs)
        else:
            return("Quantité demandée supérieure au stock disponible.")
    def clean_quantity(self):
            quantite = self.cleaned_data.get('quantite')
            
            if Product.quantite < quantite:
                raise forms.ValidationError("La quantité demandée est supérieure au stock disponible.")
            return quantite