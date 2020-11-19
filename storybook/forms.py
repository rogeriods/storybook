from django import forms
from storybook.models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'text', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'rogerio', 'type':'hidden'}),
        }
        labels = {
            'title': 'Title of your day',
            'text': '',
        }
