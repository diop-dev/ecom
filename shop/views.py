from django.shortcuts import redirect
from django.shortcuts import render
from .models import Product, Commande
from django.core.paginator import Paginator









def index(request):
    products = Product.objects.all()
    item_name =request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        products= Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(products, 4)  
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)


def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html',{'product': product_object})


def checkout (request):
    if request.method== "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays= pays, zipcode=zipcode )
        com.save()
        return redirect('confirmation')
    return render (request, 'shop/checkout.html')

def confimation (request):
    info =Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render (request, 'shop/confirmation.html',{'name':nom} )
    
   
   























