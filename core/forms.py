from django import forms
from .models import Meta
from django.utils import timezone

class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ['nome', 'especifica', 'mensuravel', 'relevante', 'tempo', 'email']

    def clean_tempo(self):
        tempo = self.cleaned_data.get('tempo')
        today = timezone.now().date()  

        if tempo < today:
            raise forms.ValidationError("A data não pode ser anterior ao dia de hoje.")
        return tempo
