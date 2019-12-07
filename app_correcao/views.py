from django.shortcuts import render
from .models import *

def Minhas_soli(request):
    fun= Funcionario.objects.get(usuario=request.user)

    solicitacoes= Solicitacao.objects.filter(solicitante = fun)

    print(solicitacoes)

    return render(request, 'app_correcao/minhaSolicitacao.html', {'solicitacoes': solicitacoes})

def TodasSoli(request):
    fun = Funcionario.objects.get(usuario=request.user)

    if fun.cargo.ehchefe:
        sol = Solicitacao.objects.all()
        return render(request, 'app_correcao/TodasSoli.html', {'sol': sol})

    else:
        return render(request, 'app_correcao/TodasSoliErro.html')