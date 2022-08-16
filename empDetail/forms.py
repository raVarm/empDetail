from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User
from . models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'username', 'email', 'phone', 'department', 'role']
        widgets = {

            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Your name',
            }),
            
            'username' : forms.TextInput(attrs={
                'placeholder' : 'Enter Your Username',
                'class' : 'form-control'
            }),

            'email' : forms.EmailInput(attrs={
                'placeholder' : 'Enter Your Mail',
                'class' : 'form-control',
                'oninvalid' : "setCustomValidity('Enter Your Crendentials Correctly!')",
                'required' : "Enter Your Email First!"
            }),

            # 'password' : forms.PasswordInput(attrs={
            #     'placeholder' : "Enter Your Password",
            #     'class' : 'form-control'
            # }),

            'phone' : forms.NumberInput(attrs={
                'placeholder' : "Enter Your Number",
                'class' : 'form-control'
            }),

            'department' : forms.TextInput(attrs={
                'placeholder' : 'Enter Department',
                'class' : 'form-control'
            }),

            'role' : forms.TextInput(attrs={
                'placeholder' : 'Enter Role',
                'class' : 'form-control'
            }),

            }
        labels = {
            'name' : 'Name' #will change the label of field
        }

        help_texts = {
            'name' : 'Please enter your name'    #will show help text below the field.
        }
        
        error_messages = {
            'name' : {
                'required' : 'First enter your name!'
            },

            'username' : {
                'required' : 'Please enter your username!'
            },

            'email' : {
                'required' : 'Please enter your email!'
            },

            'phone' : {
                'required' : 'Please enter your phone!'
            },

            'department' : {
                'required' : 'Please enter your department!'
            },

            'role' : {
                'required' : 'Please enter your role!'
            },
        }
