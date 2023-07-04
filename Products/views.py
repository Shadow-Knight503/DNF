from django.shortcuts import render, HttpResponseRedirect
from django.forms import formset_factory, modelformset_factory
from .models import Sale, Product, ProdImg, Company
from .forms import StartSale, AddProd, PdIgFrm


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


def add_product(request):
    print('Working...')
    prod = AddProd(request.POST)
    imgfrmset = formset_factory(PdIgFrm)
    imgsfrm = imgfrmset(request.POST, request.FILES or None)
    if request.method == 'POST':
        print(imgsfrm)
        for form in imgsfrm:
            print('Looping')
            print(form)
        if prod.is_valid():
            print('Validated')
            for form in imgsfrm:
                print(form.cleaned_data)
            prod.save(commit=False)
            # return HttpResponseRedirect('https://youtu.be/dQw4w9WgXcQ')
        else:
            print("Errors: ")
            print(prod.errors)
    ctx = {
        'ProdForm': AddProd,
        'PdImgForm': imgsfrm,
    }
    return render(request, "ProductAdd.html", ctx)


def test(request):
    context = {}

    # creating a formset and 5 instances of GeeksForm
    GeeksFormSet = modelformset_factory(Sale, form=StartSale, extra=3)
    formset = GeeksFormSet(request.POST, request.FILES or None)

    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)

    # Add the formset to context dictionary
    context['formset'] = formset
    return render(request, "Test.html", context)
