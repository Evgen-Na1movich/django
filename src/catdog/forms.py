from django import forms


class PetFilterForm(forms.Form):
    CHOICES = (('cat', 'KOTI'),
               ('dog', 'COBAKI'))
    pet = forms.ChoiceField(choices=CHOICES)