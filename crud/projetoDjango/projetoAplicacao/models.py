from django.db import models

# Create your models here.

from django.db import models

FUNCAO_CHOICE_SERVICO = (
    ('SPA', 'Single Page Application'),
    ('PWA', 'Progressive Web Application'),
    ('WS', 'WebSite'),
    ('SW', 'Sistema Web'),
    ('IV', 'Identidade Visual'),
)

FUNCAO_CHOICE_PARCELAMENTO = (
    (1,'01-A VISTA'),
    (2,'02'),
    (3, '03'),
    (4, '04'),
    (5, '05'),
    (6, '06'),
    (7, '07'),
    (8, '08'),
    (9, '09'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
)

FUNCAO_CHOICE_REUNIAO = (
    ('GERAL', 'GERAL'),
    ('DIRETORIA', 'DIRETORIA'),
    ('PROJETOS', 'PROJETOS'),
    ('EXTERNA', 'EXTERNA'),
)
# Create your models here.

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


class Servico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='Cliente')
    nomeServico = models.CharField('Serviço', max_length=4, choices=FUNCAO_CHOICE_SERVICO)
    descricao = models.TextField('Descrição', null=True, blank=True)
    valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    Desconto = models.DecimalField('Desconto',max_digits=6, decimal_places=2)
    parcelamento = models.IntegerField('Parcelado', choices=FUNCAO_CHOICE_PARCELAMENTO)

    def valorFinal(self):
        return str(self.valor - self.Desconto)
    def __str__(self):
        return self.nomeServico + ' - ' + str(self.cliente) + \
               ' - R$' + str(self.valor - self.Desconto) + ' - ' + str(self.parcelamento) + 'x'


class Reuniao(models.Model):
    dataReuniao = models.DateField('Data da Reunião', blank=True, null=True)
    tipoReuniao = models.CharField('Reunião', max_length=12, choices=FUNCAO_CHOICE_REUNIAO)
    descricaoReuniao = models.TextField('Descrição', null=True, blank=True)
    presenca = models.ManyToManyField('Cliente', null=True, blank=True, related_name="presenca")
    ausencia = models.ManyToManyField('Cliente', null=True, blank=True, related_name="ausencia")

    def __str__(self):
        return str(self.dataReuniao) + ' Descrição: ' + self.descricaoReuniao

