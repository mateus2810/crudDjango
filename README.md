### Comandos para criaçao de projeto django no terminal
1) Verificar versao do python -> $ python3
2) Criar pasta do projeto -> $ mkdidr "nome_do_projeto"
3) Entrar na pasta do projeto -> $ cd "nome_do_projeto"
4) Instalar virtual env na pasta -> $ python3 -m venv env
5) Se nao funcionar usar o comando -> $ sudo apt-get install python3.6-venv
6) Instalar gerenciador de pacote "pip" - $ sudo apt install python-pip
7) Apos o procedimento deve-se ativar a virtual env -> $ source env/bin/activate
8) Instalar django na virtual env -> $ pip install django
10) Criar e iniciar projeto -> $ django-admin startproject "nome_projetoApp"


### Comandos para criar primeira app
1) Criar app -> python3 manage.py startapp "nome_app"
2) Ir ao arquivo settings.py e registrar apps "nome_app" em INSTALLED_APPS
3) Apos isso definir o banco de dados, se for mysql editar no arquivo settings.py o campo de DATABASES para -> 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'schemaCrud',
        'USER': 'root',
        'PASSWORD': '', 
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
``` 

4) Se houver requirementos pip install -r requirements-dev.txt
5) Executar o comando pip install mysqlclient
6) Workbeach criar shema(colocar imagem) - colocar mesmo nome do schema no (NAME = /\)


![alt text](https://github.com/mateus2810/crudDjango/blob/master/crud/BD/workbeach1.png)
Foto 2:


![alt text](https://github.com/mateus2810/crudDjango/blob/master/crud/BD/workbeach2.png)

7) Proximo comando usa o arquivo da pasta migrations e converte pra SQL pra criar e modificar o banco ->$ python3 manage.py migrate 
8) Criar novas migrações com base nas alterações feitas(necessário apenas quando ouver alteração no banco) em seus modelos de bd -> $ python3 manage.py makemigrations
9) Rodar aplicaçao online -> python3 manage.py runserver



### CRIAÇÃO DE CRUD COM DJANGO
1) Registrar app em settings na pasta do projeto
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nomeDaAplicacao',
    'bootstrapform',
]
```
2)Criar uma nova url para o projeto em urls.py
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('nomeDaAplicacao.urls')),
]
```

3) Na pasta da aplicação crie um arquivo chamado urls.py e coloque o seguinte código
```
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [

    path('cliente/', views.cliente, name='cliente'),
    path('home/', views.home, name='home'),
    path('listarCliente/', views.listarCliente, name='listarCliente'),
    path('excluirCliente/<pk>', views.excluirCliente, name='excluirCliente'),
    path('editarCliente/<pk>', views.editarCliente, name='editarCliente')

]
```
4) Apos isto entrar na views da app digitar o codigo abaixo
```
from django.shortcuts import render, redirect
from .models import *
from projetoApp.models import *
from django.contrib import messages
#from . import models
from .forms import *

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


  ```  
5) Criar models Cliente para criar objetos do banco de dados para armazenar

```
class Cliente(models.Model):
    nome = models.CharField(('Nome'), max_length=40, null=True, blank=True)
    cidade = models.CharField(('Cidade'), max_length=80, null=True, blank=True)
    bairro = models.CharField(('Bairro'), max_length=20, null=True, blank=True)
    rua = models.CharField(('Rua'), max_length=80, null=True, blank=True)
    numero = models.CharField(('Numero'), max_length=20, null=True, blank=True)
    cep = models.CharField(('CEP'), max_length=15, null=True, blank=True)
    cpf = models.CharField(('CPF/CNPJ'), max_length=15, null=True, blank=True)
    contato = models.CharField(('Contato'), max_length=20, null=True, blank=True)
    email = models.CharField(('Email'), max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = ("Cliente")

    def __str__(self):
        return self.nome
 ```
6) Dentro da pasta Produto vc vai criar uma pasta chamada templates e vai criar o arquivo home.html
