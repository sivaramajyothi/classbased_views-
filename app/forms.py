from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=150)
    age=forms.IntegerField(min_value=20)