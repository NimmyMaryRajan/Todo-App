from django import forms
from .models import task

class taskform(forms.ModelForm):
    class Meta:
        model = task
        fields = ['task_name', 'priority', 'due_date','completed']
        widgets = {
            'due_date': forms.SelectDateWidget(),
        }
        labels = {
            'completed': 'Mark as completed'
        }

    def __init__(self, *args, **kwargs):
        super(taskform, self).__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #         field.widget.attrs.update({'class': 'input'})
        self.fields['task_name'].widget.attrs.update({'class': 'input input--text'})
        self.fields['priority'].widget.attrs.update({'class': 'input input--text'})
   #     self.fields['star'].widget.attrs.update({'class': 'input input--checkbox'})
        self.fields['due_date'].widget.attrs.update({'class': 'input--date'})
        self.fields['completed'].widget.attrs.update({'class': 'input input--checkbox'})