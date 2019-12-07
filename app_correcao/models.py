from django.db import models
from django.contrib.auth.models import User

class Cargo(models.Model):
    nome = models.CharField(max_length=120)
    ehchefe = models.BooleanField(default=False)
    ehmotorista = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=120)
    cod = models.CharField(max_length=4)
    ehtransporte = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=120)
    matricula = models.CharField(max_length=10)
    cargo = models.ForeignKey(Cargo,on_delete=models.SET_NULL,null=True,blank=True)
    departamento = models.ForeignKey(Departamento,on_delete=models.SET_NULL,null=True,blank=True)
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.descricao

class Solicitacao(models.Model):
    solicitante = models.ForeignKey(Funcionario,on_delete=models.SET_NULL,null=True,blank=True)
    origem = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    datahora = models.DateTimeField()
    qt_passageiros = models.CharField(max_length=130,null= True,blank=True)

    def __str__(self):
        return self.destino

class Atendimento(models.Model):
    veiculo = models.ForeignKey(Veiculo,on_delete=models.SET_NULL,null=True,blank=True)
    solicitacao = models.ForeignKey(Solicitacao,on_delete=models.SET_NULL,null=True,blank=True)
    responsavel = models.ForeignKey(Funcionario,on_delete=models.SET_NULL,null=True,blank=True)

