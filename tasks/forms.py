from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form class for users to create a task
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'estimated_minutes', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short descriptive title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Optional task details'}),
            'estimated_minutes': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'Estimated task duration (e.g. 30)'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_estimated_minutes(self):
        value = self.cleaned_data.get('estimated_minutes')
        # Allow empty (none) but if provided must be > 0
        if value is not None and value <= 0:
            raise forms.ValidationError("Estimated minutes must be greater than 0.")
        return value
