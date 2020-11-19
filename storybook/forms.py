from django import forms
from storybook.models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Title of your day',
            'text': '',
        }
