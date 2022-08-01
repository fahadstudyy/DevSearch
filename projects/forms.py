from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Project
class projectform(ModelForm):
    class Meta():
        model = Project
        fields = ['title', 'image', 'describe', 'demo_link', 'source_link', 'tag']
        Widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
            super(projectform, self).__init__(*args, **kwargs)

            for name,field in self.fields.items():
                field.widget.attrs.update({'class':'input'})
            # self.fields['title'].widget.attrs.update({'class':'input'})
