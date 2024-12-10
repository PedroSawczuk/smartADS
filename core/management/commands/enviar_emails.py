from django.core.mail import send_mail
from django.utils.timezone import now
from django.core.management.base import BaseCommand
from models import Meta

class Command(BaseCommand):
    help = 'Envia e-mails para as metas com data final de hoje'

    def handle(self, *args, **kwargs):
        hoje = now().date()
        metas = Meta.objects.filter(tempo=hoje)
        for meta in metas:
            send_mail(
                subject=f'Lembrete: Meta SMART - {meta.nome}',
                message=f'Sua meta "{meta.nome}" tem o prazo final hoje!\n\nDescrição: {meta.especifica}',
                from_email='seuemail@dominio.com',  
                recipient_list=[meta.email],
            )
        self.stdout.write(f"{metas.count()} e-mails enviados.")
