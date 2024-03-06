from django.shortcuts import render, redirect
from main import models

def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/index.html', context)


# CRUD 

# Create
# Read -> List/Detail
# Update
# Delte

def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/banner/create.html')


def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)

# --------------------------------------------------------------------------

def create_price(request):
    if request.method == "POST":
        title = request.POST['title']
        price = request.POST['price']
        body = request.POST['body']
        models.Price.objects.create(
            title=title,
            price=price,
            body=body,
        )
    return render(request, 'dashboard/price/create.html')


def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices':prices
    }
    return render(request, 'dashboard/price/list.html', context)

# ---------------------------------------------------------------------------

def create_about(request):
    if request.method == "POST":
        body = request.POST['body']
        models.AboutUs.objects.create(
            body=body,
        )
    return render(request, 'dashboard/about_us/create.html')


def list_about(request):
    abouts = models.AboutUs.objects.all()
    context = {
        'abouts':abouts
    }
    return render(request, 'dashboard/about_us/list.html', context)

# ------------------------------------------------------------------

def create_service(request):
    if request.method == "POST":
        name = request.POST['name']
        body = request.POST['body']
        icon = request.POST['icon']
        models.Service.objects.create(
            name=name,
            body=body,
            icon=icon,
        )
    return render(request, 'dashboard/services/create.html')


def list_service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'dashboard/services/list.html', context)