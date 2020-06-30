Comandos para criaçao de projeto django no terminal
1) Verificar versao do python -> $ python3
2) Criar pasta do projeto -> $ mkdidr "nome_do_projeto"
3) Entrar na pasta do projeto -> $ cd "nome_do_projeto"
4) Instalar virtual env na pasta -> $ python3 -m venv env
5) Se nao funcionar usar o comando -> $ sudo apt-get install python3.6-venv
6) Instalar gerenciador de pacote "pip" - $ sudo apt install python-pip
7) Apos o procedimento deve-se ativar a virtual env -> $ source env/bin/activate
8) Instalar django na virtual env -> $ pip install django
10) Criar e iniciar projeto -> $ django-admin startproject "nome_projetoApp"


Comandos para criar primeira app
1) Criar app -> python3 manage.py startapp "nome_app"
2) Ir ao arquivo settings.py e registrar apps "nome_app" em INSTALLED_APPS
3) Apos isso definir o banco de dados, se for mysql editar no arquivo settings.py o campo de DATABASES para -> 
DATABASES = {
    'default': {
    
        'ENGINE': 'django.db.backends.mysql',
        
        'NAME': 'ES',
       
        'USER': 'alexlr',
        
        'PASSWORD': '91851007',
        
        'HOST': '127.0.0.1',
        
        'PORT': '3306',
    }
}
4) Se houver requirementos pip install -r requirements-dev.txt
5) Executar o comando pip install mysqlclient
6) Workbeach criar shema(colocar imagem) - colocar mesmo nome do schema no (NAME = /\)
7) Proximo comando usa o arquivo da pasta migrations e converte pra SQL pra criar e modificar o banco ->$ python3 manage.py migrate 
8) Criar novas migrações com base nas alterações feitas em seus modelos de bd -> $ python3 manage.py makemigrations
9) Rodar aplicaçao online -> python3 manage.py runserver

