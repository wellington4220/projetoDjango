from django.db import models

from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    duracao = models.DurationField()  # Exemplo: "00:30:00" para 30 minutos

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("confirmado", "Confirmado"),
        ("cancelado", "Cancelado"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pendente")

    def __str__(self):
        return f"{self.cliente} - {self.servico} em {self.data_hora}"

from django.db import models

# models de agendamento
class Agendamento(models.Model):
    nome = models.CharField(max_length=100)  # Nome do cliente
    telefone = models.CharField(max_length=15)  # Telefone para contato
    servico = models.CharField(
        max_length=50,
        choices=[
            ("Corte de Cabelo", "Corte de Cabelo"),
            ("Barba", "Barba"),
            ("Corte + Barba", "Corte + Barba"),
            ("Sobrancelha", "Sobrancelha"),
        ],
    )  # Serviço escolhido
    data_hora = models.DateTimeField()  # Data e hora do agendamento

    def __str__(self):
        return f"{self.nome} - {self.servico} ({self.data_hora})"

