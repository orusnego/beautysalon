from django.forms import ModelForm, Textarea
from django import forms
from .models import Appointment

class AppointmentForm(ModelForm):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['phone'].widget.attrs.update(        
            {'class': 'form-control'})
            

    class Meta:
        model = Appointment
        fields = ['first_name','last_name','phone']
        widgets = {
            'first_name': Textarea(attrs={'rows': 1, 'cols': 30}),
            'last_name': Textarea(attrs={'rows': 1}),
            'phone': Textarea(attrs={'rows': 1}),
        }
        def clean_time(self):
            time = self.cleaned_time['time']
            if Appointment.objects.filter(time=time).exists():
                raise forms.ValidationError("Это время занято!.")
            return time
        

