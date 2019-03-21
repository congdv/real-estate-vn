from django import forms

from .models import RealEstateProject


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea)
