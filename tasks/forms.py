from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form class for users to create a task
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'estimated_minutes', 'due_date', 'completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional task details'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'title',
            'description',
            'estimated_minutes',
            'due_date',
            Field('completed', css_class="form-check-input"),
        )

    def clean_estimated_minutes(self):
        value = self.cleaned_data.get('estimated_minutes')
        # Allow empty (none) but if provided must be > 0
        if value is not None and value <= 0:
            raise forms.ValidationError("Estimated minutes must be greater than 0.")
        return value
