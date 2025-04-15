# rota para home
from django.urls import path
from . import views
from django.urls import path
# rota para serviços
urlpatterns = [
    path("", views.home, name="home"),
    path("servicos/", views.servicos, name="servicos"),
     path('agendar/', views.agendar_view, name='agendar'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    #path('clientes/verificar-email/', views.verificar_email, name='verificar_email'),
    path('clientes/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:cliente_id>/', views.excluir_cliente, name='excluir_cliente'),
]
