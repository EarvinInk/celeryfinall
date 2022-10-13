from django import forms


class GenerateRandomCSVForm(forms.Form):
    filename = forms.CharField()
    data_count = forms.IntegerField()
