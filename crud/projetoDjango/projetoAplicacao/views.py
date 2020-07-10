from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from projetoApp.models import *
from django.contrib import messages
#from . import models
from .forms import *

# Create your views here.

def cliente(request):
    cliente = Cliente.objects.all()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso')
            return redirect('cliente')
    form = ClienteForm()
    context = { 'form': form,
                'cliente': cliente
                        }
    return render(request, 'cliente.html', context)

def home(request):

    return render(request, 'home.html')

def listarCliente(request):
    cliente = Cliente.objects.all()
    form = ClienteForm()
    context = {'form': form,
               'cliente': cliente
               }
    return render(request, 'listarCliente.html', context)

def excluirCliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    messages.error(request, 'Cadastro removido com sucesso')

    return redirect( 'listarCliente' )

def editarCliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        messages.success(request, 'Editado')
        return redirect('cliente')
    context = { 'form': form, 'cliente': cliente }
    return render(request, 'editarCliente.html', context)