from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    param_sort= request.GET.get('sort','no_sort')
    context = {}
    if param_sort == 'no_sort':
        phones = Phone.objects.all()
    elif param_sort == 'name':
        phones = Phone.objects.order_by('name')
    elif param_sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif param_sort == 'max_price':
        phones = Phone.objects.order_by('-price')


    print(param_sort)
    context['phones'] = phones
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone = get_object_or_404(Phone,slug = slug)
    context['phone'] = phone
    return render(request, template, context)
