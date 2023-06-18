from django import forms

class SignupFrom(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    contact=forms.CharField(max_length=10)
    password=forms.CharField()