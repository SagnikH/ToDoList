from django import forms

from .models import RecordList

class RecordListForm(forms.ModelForm) :

    class Meta :
        model = RecordList
        fields = [
                'todo',
        ]