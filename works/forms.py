from django import forms
from .models import Work, Companies


class WorkFrorm(forms.Form):
    description = forms.CharField(max_length=200)
    company = forms.ModelChoiceField(queryset=Companies.objects.all())

    description.widget.attrs.update({'class': 'form-control'})
    company.widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_work = Work.objects.create(
            description=self.cleaned_data['description'],
            company=self.cleaned_data['company'],
        )
