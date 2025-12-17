from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form class for users to create and edit tasks.

    This form is used for both task creation and updating,
    allowing user to manage task details such as due date,
    estimated time, and completion status.
    """
    class Meta:
        """
        Specify the django model and fields used in the form.
        """
        model = Task
        fields = [
            'title',
            'description',
            'estimated_minutes',
            'due_date',
            'completed'
            ]
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder':
                'Optional task details'
                }),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with Crispy Forms helper and layout.

        Disables automatic form tag rendering so the form can
        be embedded within custom templates.
        """
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
        """
        Validate the estimated_minutes field.

        Ensures the value is greater than zero if provided.
        """
        value = self.cleaned_data.get('estimated_minutes')
        if value is not None and value <= 0:
            raise forms.ValidationError(
                "Estimated minutes must be greater than 0."
                )
        return value
