from django import forms

from work.models import Todo
import datetime 

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        exclude = ['user','project','pub_date']
        
    def save(self, user=None, project=None, *kw):
        if self.instance.pk:
            i = self.instance
            i.title = self.cleaned_data.get('title')
            i.desc = self.cleaned_data.get('desc','')
            i.type = self.cleaned_data.get('type')
            i.status = self.cleaned_data.get('status')
            i.deadline = self.cleaned_data.get('deadline')
            i.is_public = self.cleaned_data.get('is_public')
        else:
            d = {
                'user': user,
                'project': project,
                'title': self.cleaned_data.get('title'),
                'desc': self.cleaned_data.get('desc',''),
                'type': self.cleaned_data.get('type'),
                'status': self.cleaned_data.get('status'),
                'pub_date': datetime.datetime.now(),
                'deadline': self.cleaned_data.get('deadline'),
                'is_public': self.cleaned_data.get('is_public'),
            }
            i = Todo(**d)
        i.save()
        return i