from django import forms
from django.forms import fields, widgets
from .models import todomodel
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

<div style="width:312px;max-width:100%;"><div style="height:0;padding-bottom:55.77%;position:relative;"><iframe width="312" height="174" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameBorder="0" src="https://imgflip.com/embed/5be81p"></iframe></div><p><a href="https://imgflip.com/gif/5be81p">via Imgflip</a></p></div>

class todoform(forms.ModelForm):
    title=forms.CharField(label_suffix = ' ',widget =forms.TextInput(attrs={'class':'form-control'}))
    # desc = forms.CharField(label_suffix= ' ')
    class Meta:
        model = todomodel
        fields = ['title','desc','startdate','enddate']

        widgets={
            # 'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs= {'class':'form-control'}),
            'startdate':DateInput(attrs={'class':'form-control'}),
            'enddate':DateInput(attrs={'class':'form-control'})
        }

class usersign(UserCreationForm):
    password1 = forms.CharField(label_suffix = ' ',label='Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label_suffix = ' ',label='Confirm Password (again) ',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(label_suffix = ' ',widget = forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label_suffix = ' ',widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(label_suffix = ' ',widget = forms.TextInput(attrs={'class':'form-control'}))
    email= forms.CharField(label_suffix = ' ',widget = forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User

        fields = ['username','email','first_name','last_name']
        labels = {'first_name':'First Name','username':'User Name','last_name':'Last Name'}

class userlogin(AuthenticationForm):
    username = username = forms.CharField(label_suffix = ' ',widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label_suffix = ' ',label='Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','password']
        
