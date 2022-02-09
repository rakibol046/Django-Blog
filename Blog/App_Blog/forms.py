from dataclasses import fields
import imp
from statistics import mode
from django import forms
from App_Blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model =  Comment
        fields = ('comment',)
