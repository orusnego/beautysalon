from django.forms import ModelForm, Textarea
from django import forms
from .models import Review

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['text'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['rate'].widget.attrs.update(        
            {'class': 'form-control'})
        self.fields['rate'].widget.empty_label = "Оценка не выбрана"
    class Meta:
        model = Review
        fields = ['name','rate','text']
        widgets = {
            'name': Textarea(attrs={'rows': 1, 'cols': 30}),
            'text': Textarea(attrs={'rows': 4}),
        }