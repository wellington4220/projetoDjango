from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cliente, Servico, Agendamento
from .models import Agendamento
admin.site.register(Cliente)
admin.site.register(Servico)
admin.site.register(Agendamento)

