from django.core.mail import send_mail
from django.utils.timezone import localtime
from django.utils import timezone
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Meta
from .forms import MetaForm

class CriarMetaView(SuccessMessageMixin, CreateView):
    model = Meta
    form_class = MetaForm
    template_name = 'metas/criar_meta.html'
    success_url = reverse_lazy('criar_meta')
    success_message = "Meta criada com sucesso!"

    def form_valid(self, form):
        meta = form.save()

        nome_meta = meta.nome
        tempo_meta = meta.tempo
        usuario_email = meta.email

        dias_restantes = (tempo_meta - localtime(timezone.now()).date()).days

        subject = f"Sua meta '{nome_meta}' foi criada!"
        message = f"""
            Olá!

            Sua meta '{nome_meta}' foi criada com sucesso! 

            A data de conclusão da sua meta é {tempo_meta.strftime('%d/%m/%Y')}. 
            Faltam apenas {dias_restantes} dias para o prazo! 

            No final desse prazo, você receberá um email sobre essa meta criada!

            Abraços,
            José Estêvão, Pedro Sawczuk e Reginaldo Júnior.
        """
        
        send_mail(subject, message, 'smartadsif@gmail.com', [usuario_email])

        if not meta.email_enviado and dias_restantes <= 1:  
            reminder_subject = f"Última chance! Sua meta '{nome_meta}' está quase vencendo!"
            reminder_message = f"""
                Olá!

                Faltam apenas {dias_restantes} dias para a sua meta '{nome_meta}'! O prazo final é {tempo_meta.strftime('%d/%m/%Y')}. 

                Não deixe para última hora, estamos aqui para ajudar você a alcançar sua meta!

                Abraços,
                José Estêvão, Pedro Sawczuk e Reginaldo Júnior.
            """
            send_mail(reminder_subject, reminder_message, 'smartadsif@gmail.com', [usuario_email])
            
            meta.email_enviado = True
            meta.save()

        subject_admin = f"Novo usuário criou uma meta: '{nome_meta}'"
        message_admin = f"""
            Olá!

            O usuário com o e-mail {usuario_email} criou a meta '{nome_meta}'.

            A data de conclusão da meta é {tempo_meta.strftime('%d/%m/%Y')}.
        """
        send_mail(subject_admin, message_admin, 'smartadsif@gmail.com', ['smartadsif@gmail.com'])

        return super().form_valid(form)
