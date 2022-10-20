from django import forms
from .models import StudentDB

class StdForm(forms.ModelForm):
    class Meta:
        model = StudentDB
        fields = ('std_roll_no', 'std_name', 'std_class')

        
