from django import forms
from .models import Idea


class IdeaForm(forms.ModelForm):
    """
    Form class for users to submit productivity blog ideas.

    This form allows visitors (authenticated or not) to suggest
    blog topics, which are stored for later admin review.
    """
    class Meta:
        """
        Specifiy the django model and order of the fields.
        """
        model = Idea
        fields = ['title', 'body', 'submitter_name', 'submitter_email']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'submitter_name': forms.TextInput(attrs={'class':'form-control'}),
            'submitter_email': forms.EmailInput(attrs={'class':'form-control'}),
        }
