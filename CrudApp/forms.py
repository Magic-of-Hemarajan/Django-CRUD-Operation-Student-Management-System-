from django import forms
from .models import StudentModels
    
class StudentForms(forms.ModelForm):
    class Meta:
        model = StudentModels
        fields = '__all__'

        widgets = {
            'Name':  forms.TextInput(attrs={'class':'student', 'required':'required'}),
            'Father_Name':  forms.TextInput(attrs={'class':'student', 'required':'required'}),
            'Mother_Name':  forms.TextInput(attrs={'class':'student', 'required':'required'}),
            'Age':  forms.NumberInput(attrs={'class':'student', 'required':'required'}),
            'College_Name':  forms.TextInput(attrs={'class':'student','required':'required'}),
            'Department':  forms.TextInput(attrs={'class':'student', 'required':'required'}),
            'Address':  forms.Textarea(attrs={'class':'student', 'required':'required'}),
            'Email':  forms.EmailInput(attrs={'class':'student', 'required':'required'}),
            'Phone_Number':  forms.NumberInput(attrs={'class':'student', 'required':'required'}),
            'Upload_images':  forms.ClearableFileInput(attrs={'class':'student', 'required':'required'}),
        }
