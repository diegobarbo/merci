from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Peca


@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')


@login_required
def pecas(request):
    return render(request, 'dashboard/pecas.html')


@login_required
def vendas(request):
    return render(request, 'dashboard/vendas.html')
