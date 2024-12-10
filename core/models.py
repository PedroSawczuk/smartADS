from django.db import models
from django.utils import timezone

class Meta(models.Model):
    nome = models.CharField("Nome da Meta", max_length=200)
    especifica = models.TextField("Específica", help_text="Descreva a meta de forma específica.")
    mensuravel = models.TextField("Mensurável", help_text="Como você medirá o progresso?")
    atingivel = models.TextField("Atingível", help_text="Por que essa meta é realista?")
    relevante = models.TextField("Relevante", help_text="Qual a importância dessa meta?")
    tempo = models.DateField("Data Final", help_text="Data limite para alcançar a meta.")
    email = models.EmailField("E-mail", help_text="Receberá o lembrete sobre a meta.")
    criado_em = models.DateTimeField(auto_now_add=True)
    email_enviado = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.nome
