from django.contrib import admin
from .models import *


admin.site.register(Cargo)

admin.site.register(Departamento)
admin.site.register(Funcionario)
admin.site.register(Veiculo)
admin.site.register(Solicitacao)
admin.site.register(Atendimento)