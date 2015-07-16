from django import forms


class ListStringsForm(forms.Form):
    strings = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'enter string lines separated by newline'}))