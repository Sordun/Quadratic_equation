from django import forms


class CalculatorForm(forms.Form):
    a = forms.CharField()
    b = forms.CharField()
    c = forms.CharField()


class GuessForm(forms.Form):
    guess = forms.CharField()
