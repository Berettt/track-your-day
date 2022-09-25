from dataclasses import field
from django import forms
from .models import TaskDay
class Task(forms.ModelForm):
    class Meta:
        model = TaskDay
        fields = '__all__'
