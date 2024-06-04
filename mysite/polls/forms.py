from django.forms import ModelForm, TextInput, NumberInput

from .models import Survey


class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'
        labels = {
            "user_name": "User NAME",
            "user_age": "User Age"
        }
        widgets = {
            'user_name': TextInput(attrs={'class': 'form-control'}),
            'user_age': NumberInput(attrs={'class': 'form-control'}),
        }