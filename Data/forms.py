from django import forms
from .models import Years, YEARS



class YearsForm(forms.ModelForm):
    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}
    year = forms.ChoiceField(choices = YEARS, required = True,
                               widget = forms.Select(attrs = attrs))
    class Meta:
        model = Years
        fields = ['year']
