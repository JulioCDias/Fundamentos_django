from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Transacao
from .forms import TransacaoForm
import datetime


# Create your views here.

def home(request):
    data = {}
    data['transacoes'] = ['transacao1', 'transacao2', 'transacao3']
    data['data'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)

def update(request, id):
    data = {}
    transacao = Transacao.objects.get(pk=id)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('listagem')
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, id):
    data = {}
    transacao = Transacao.objects.get(pk=id)
    transacao.delete()
    return redirect('listagem')
