from django import forms
from .models import Image, Profile

class ProfileForm(forms.ModelForm):
    """
    class facilitates the creation of profile form objects
    """
    class Meta:
        model = Profile
        exclude = ['user']