from django import forms
from django.core import validators

def  check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with Z")   

class FormName(forms.Form):
    name = forms.CharField(label='Name', max_length=128, validators=[check_for_z])
    email = forms.EmailField(label='Email')
    verify_email = forms.EmailField(label='Verify Email')
    text = forms.CharField(label='Text', widget=forms.Textarea)

    

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError("Make sure emails match!")

    
