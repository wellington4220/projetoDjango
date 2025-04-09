from django.shortcuts import render
from .models import Cliente, Servico, Agendamento
from django.shortcuts import render, redirect
from .models import Cliente
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cliente
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json




def home(request):
    return render(request, "agendamentos/home.html")

def servicos(request):
    return render(request, "agendamentos/servicos.html")

def agendar_view(request):
    # Dados buscados do banco
    clientes = Cliente.objects.all()
    servicos = Servico.objects.all()

    context = {
        'clientes': clientes,
        'servicos': servicos,
    }

    return render(request, 'agendamentos/agendar.html', context)

from django.db import IntegrityError
# adicionando clientes
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Cliente
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Cliente
from django.shortcuts import render, get_object_or_404
import json

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/adicionar_cliente.html', {'clientes': clientes})

@csrf_exempt
@csrf_exempt
def adicionar_cliente(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            Cliente.objects.create(
                nome=data.get('nome'),
                telefone=data.get('telefone'),
                email=data.get('email')
            )
            return JsonResponse({'sucesso': True})
        except IntegrityError:
            return JsonResponse({'sucesso': False, 'erro': 'Este email já está cadastrado.'})
        except Exception as e:
            return JsonResponse({'sucesso': False, 'erro': str(e)})
    return JsonResponse({'erro': 'Método inválido'}, status=400)

@csrf_exempt
def editar_cliente(request, cliente_id):
    if request.method == 'PUT':
        cliente = get_object_or_404(Cliente, id=cliente_id)
        data = json.loads(request.body)
        cliente.nome = data.get('nome')
        cliente.telefone = data.get('telefone')
        cliente.email = data.get('email')
        try:
            cliente.save()
            return JsonResponse({'sucesso': True})
        except IntegrityError:
            return JsonResponse({'sucesso': False, 'erro': 'Este email já está cadastrado.'})
        except Exception as e:
            return JsonResponse({'sucesso': False, 'erro': str(e)})
    return JsonResponse({'erro': 'Método inválido'}, status=400)

@csrf_exempt
def excluir_cliente(request, cliente_id):
    if request.method == 'DELETE':
        cliente = get_object_or_404(Cliente, id=cliente_id)
        cliente.delete()
        return JsonResponse({'sucesso': True})
    return JsonResponse({'erro': 'Método inválido'}, status=400)