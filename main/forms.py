from django import forms

class CrearBoleta(forms.Form):
    cliente = forms.CharField(max_length=200, required=False)
    total = forms.DecimalField(max_digits=10, decimal_places=2)
    detalle = forms.CharField(max_length=300, required=False)