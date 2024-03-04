from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView

from .models import About, Category, Package
import asyncio
from .telegram_message import main

def index(request):
    model = About.objects.get(pk=1)
    categories = Category.objects.all()
    packages = Package.objects.all().order_by('price')[:3]
    popular = Package.objects.all().order_by('-price')[1:5]
    best_popular = Package.objects.all().order_by('-price')[0]

    data = {
        'model': model,
        'categories': categories,
        'packages': packages,
        'popular': popular,
        'best_popular':best_popular,
            }
    return render(request, 'myapp/index.html', context=data)

def about(request):
    model = About.objects.get(pk=1)

    data = {'model': model}

    return render(request, 'myapp/about.html', context=data)

def services(request):
    categories = Category.objects.all()

    data = {'categories': categories}
    return render(request, 'myapp/services.html', context=data)


def packages(request):
    search_packages = ''
    categories = Category.objects.all()
    packages = Package.objects.all()

    if request.method == 'GET':
        qidiruv_value = request.GET.get('qidiruv', None)
        if qidiruv_value is not None:
            search_packages = Package.objects.filter(country=qidiruv_value)


    data = {
        'categories': categories,
        'packages': packages,
        'search_packages': search_packages,
    }
    return render(request, 'myapp/packages.html', context=data)


def contact(request):
    if request.method == 'POST':
        ism = request.POST.get('ism')
        email = request.POST.get('email')
        mavzu = request.POST.get('mavzu')
        izoh = request.POST.get('izoh')

        asyncio.run(main(f"Ismi: {ism}\n\nEmail: {email}\n\nMavzu: {mavzu}\n\nIzoh: {izoh}"))
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'myapp/contact.html')

def show_cat(request, id):
    category = get_object_or_404(Category, pk=id)
    categories = Category.objects.all()
    packages = category.packages.all()

    data = {
        'category': category,
        'categories': categories,
        'packages': packages,
    }

    return render(request, 'myapp/packages.html', context=data)

class aboutView(DetailView):
    model = Package
    template_name = 'myapp/about_package.html'
    context_object_name = 'package'

def search(request):
    return render(request, 'myapp/search.html')

def profile_about(request, id):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            Profile.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ProfileForm()

    data = {
        'form': form
    }
    return render(request, 'myapp/profile.html', context=data)

