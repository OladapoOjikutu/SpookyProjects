from django.forms import ModelForm
from .models import NameField
from django import forms
from .models import site_visitor

class Name(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",

   "placeholder":"Enter Name You Are Called in Here" }))

    email= forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control",

   "placeholder":"Enter Your Email Address" }))
           

    class Meta():
        model = NameField
        fields = ['name', 'email']
        exclude = ('thisresult','thisresult1','thisresult2','thisresult3','thisresult4','thisresult5','thisresult6','thisresult7','thisresult8','thisresult9',)
