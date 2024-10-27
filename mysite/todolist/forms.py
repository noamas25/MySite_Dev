from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["owner","content","deadline"]
        