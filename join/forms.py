from django import forms

from join.models import Campo

class CampoForm(forms.ModelForm):
    class Meta:
        model = Campo
        fields = '__all__'