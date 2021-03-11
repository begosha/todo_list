from django import forms

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'details', 'status', 'completion_date')


