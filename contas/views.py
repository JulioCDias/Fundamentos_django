from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    data = {}
    data['transacoes'] = ['transacao1', 'transacao2', 'transacao3']
    data['data'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)