from dataclasses import fields
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


# class PictureForm(forms.ModelForms):
#     class Meta:
#         model = Post
#         fields = '__all__'
        
