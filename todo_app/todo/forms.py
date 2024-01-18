from django import forms
from .models import TodoModel

class CreateTaskModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = [
            "title",
            "description",
            "status"
            ]
        def __init__(self, *args, **kwargs):
            super(CreateTaskModelForm, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs['class'] = 'form-body-title'