from django.shortcuts import render
from .models import Sale, Product, ProdImg, Company


def home(request):
    sales = Sale.objects.all()
    products = Product.objects.all()
    comps = Company.objects.all()
    ctx = {
        'sales': sales,
        'products': products,
        'comps': comps,
    }
    return render(request, "Home.html", ctx)


def product(request, prod_id):
    prod = Product.objects.get(id=prod_id)
    ctx = {
        "prod": prod
    }
    return render(request, "ProductPage.html", ctx)


def company(request, comp_id):
    prods = Product.objects.filter(Comp=comp_id)
    comp = Company.objects.get(id=comp_id)
    ctx = {
        "comp": comp,
        "prods": prods,
    }
    return render(request, "CompanyPage.html", ctx)
