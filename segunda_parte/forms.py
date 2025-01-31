from django.forms import ModelForm
from . import models

class PlatoTipicoForm(ModelForm):
    class Meta:
        model = models.PlatoTipico
        fields = ['nombre','stock','puntaje','categoria']