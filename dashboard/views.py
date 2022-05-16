from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Peca, Venda
from .forms import PecaForm, VendaForm
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def index(request):
    vendas = Venda.objects.all()
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = VendaForm()
    context = {
        'vendas': vendas,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def staff(request):
    workers = User.objects.all()
    context = {
        'workers': workers
    }
    return render(request, 'dashboard/staff.html', context)


@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required
def pecas(request):
    items = Peca.objects.all()  # using orm
    # items = Peca.objects.raw('SELECT * FROM dashboard_peca')

    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            peca_nome = form.cleaned_data.get('nome')
            messages.success(request, f'{peca_nome} foi adicionado(a)!')
            return redirect('dashboard-pecas')
    else:
        form = PecaForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/pecas.html', context)


@login_required
def peca_delete(request, pk):
    item = Peca.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-pecas')
    return render(request, 'dashboard/peca_delete.html')


@login_required
def peca_update(request, pk):
    item = Peca.objects.get(id=pk)
    if request.method == 'POST':
        form = PecaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-pecas')
    else:
        form = PecaForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/peca_update.html', context)


@login_required
def vendas(request):
    vendas = Venda.objects.all()
    context = {
        'vendas': vendas,
    }
    return render(request, 'dashboard/vendas.html', context)
