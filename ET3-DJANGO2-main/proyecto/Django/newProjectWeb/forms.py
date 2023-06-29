from django.forms import ModelForm
from .models import Usuario, tipoForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"


