from django.shortcuts import render
from .models import Link


def home(request):
    context = {
        'links': Link.objects.all(),
        'ADMIN': Link.objects.filter(role = "ADMIN" ),
        'FINANCE_ADMIN': Link.objects.filter(role = "FINANCE_ADMIN" ),
        'HR_ADMIN': Link.objects.filter(role = "HR_ADMIN" ),
        'SALES_ADMIN': Link.objects.filter(role = "SALES_ADMIN" ),
        'ENGG_ADMIN': Link.objects.filter(role = "ENGG_ADMIN" )
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
