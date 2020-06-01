from django import forms
from .models import Image, Profile, Comments
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    """
    class facilitates the creation of profile form objects
    """
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    """
    class facilitates the creation of image form objects
    """
    class Meta:
        model = Image
        exclude = ['profile', 'likes', 'pub_date']

class CommentsForm(forms.ModelForm):
    """
    class facilitates the creation of comments form objects
    """
    class Meta:
        model = Comments
        fields = ['comment']