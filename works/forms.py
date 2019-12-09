from django import forms

from .models import Work, Companies, WorkPlace, Worker, WorkTime

class WorkFrorm(forms.Form):
    description = forms.CharField(max_length=200, label='Description work: ')
    company = forms.ModelChoiceField(queryset=Companies.objects.all(), label='Company: ')

    description.widget.attrs.update({'class': 'form-control'})
    company.widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_work = Work.objects.create(
            description=self.cleaned_data['description'],
            company=self.cleaned_data['company'],
        )

class SetWorkPlace(forms.Form):
    work_name = forms.ModelChoiceField(
        queryset=Work.objects.filter(is_active=1), 
        label='Work name:')

    worker = forms.ModelChoiceField(
        queryset=Worker.objects.all(),
        label='Set worker:')

    work_name.widget.attrs.update({'class': 'form-control'})
    worker.widget.attrs.update({'class': 'form-control'})

    def save(self):
        work_place = WorkPlace.objects.create(
            work_name=self.cleaned_data['work_name'],
            worker=self.cleaned_data['worker'],
        )

class WorkTimeForm(forms.Form):
    date_start = forms.DateField()
    date_end = forms.DateField()
    status = forms.ModelChoiceField(queryset=WorkPlace.objects.all())

    def save(self):
        new_work = WorkTime.objects.create(
            date_start=self.cleaned_data['date_start'],
            status=self.cleaned_data['date_end'],
            date_end=self.cleaned_data['status'],
        )

    # def __init__(self, user_id, *args, **kwargs):
    #     super(WorkTimeForm, self).__init__(*args, **kwargs)
    #     self.fields['foo_select'].queryset = WorkPlace.objects.get('worker.id' == user_id)
        
        
