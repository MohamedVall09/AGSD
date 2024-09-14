from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Client, Fournisseur
from .forms import ProductForm, OrderForm, ClientForm, FournisseurForm
from django.contrib.auth.models import User
from django.contrib import messages

# @login_required(login_url='user-login')
@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {'orders': orders, 'form': form, 'products': products}
    return render(request, 'dashboard/index.html', context)


# @login_required(login_url='user-login')
@login_required
def staff(request):
    workers = User.objects.all()
    context = {'workers': workers}
    return render(request, 'dashboard/staff.html', context)


def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    context = {'worker': worker}
    return render(request, 'dashboard/staff_detail.html', context)

def client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client added successfully.')
            return redirect('/client/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ClientForm()
    cls = Client.objects.all()
    return render(request, 'dashboard/client.html', {'form': form, 'cls': cls})

# def client_detail(request, pk):
#     cl = Client.objects.get(id=pk)
#     context = {'cl': cl}
#     return render(request, 'dashboard/client_detail.html', context)


def client_update(request, pk):
    cl = Client.objects.get(id=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=cl)
        if form.is_valid():
            form.save()
            return redirect('dashboard-client')
    else:
        form = ClientForm(instance=cl)
    context = {'form': form}
    return render(request, 'dashboard/client_update.html', context)

def client_delete(request, pk):
    cl = Client.objects.get(id=pk)
    if request.method == 'POST':
        cl.delete()
        return redirect('dashboard-client')
    return render(request, 'dashboard/client_delete.html')


# @login_required(login_url='user-login')
@login_required
def product(request):
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {'items': items, 'form': form}
    return render(request, 'dashboard/product.html', context)


def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')


def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {'form': form}
    return render(request, 'dashboard/product_update.html', context)


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('dashboard-product')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }
    return render(request, 'dashboard/product_add.html', context)


@login_required(login_url='user-login')
@login_required
def order(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'dashboard/order.html', context)


# def transaction(request):
#     transactions = Transaction.objects.all()
#     context = {'transactions': transactions}
#     return render(request, 'dashboard/transaction.html', context)

def fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client added successfully.')
            return redirect('/fournisseur/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = FournisseurForm()
    fls = Fournisseur.objects.all()
    return render(request, 'dashboard/fournisseur.html', {'form': form, 'fls': fls})

def fournisseur_update(request, pk):
    fl = Fournisseur.objects.get(id=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fl)
        if form.is_valid():
            form.save()
            return redirect('dashboard-fournisseur')
    else:
        form = FournisseurForm(instance=fl)
    context = {'form': form}
    return render(request, 'dashboard/fournisseur_update.html', context)

def fournisseur_delete(request, pk):
    fl = Fournisseur.objects.get(id=pk)
    if request.method == 'POST':
        fl.delete()
        return redirect('dashboard-fournisseur')
    return render(request, 'dashboard/fournisseur_delete.html')

