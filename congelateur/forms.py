from dal import autocomplete
from django import forms
from client.models import *

class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ("clientReceveur", 'montant', 'mode')
        labels = {
            'clientReceveur':('Demander la somme à'),
            'montant':('Montant souhaité'),
            'mode':('Je rembourse à l\'aide de')
        }



        """widgets = {
            "clientReceveur":autocomplete.ModelSelect2(url='client-autocomplete')
        }"""