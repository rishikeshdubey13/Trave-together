from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
        def __init__(self,*args,**kwargs):
            super(RegisterForm,self).__init__(*args,**kwargs)

            self.fields['first_name'].widget.attrs.update({
                # 'id':"form3Example3",
                'class':'form-control form-control-lg',
                'placeholder':'Enter first name'
            })
            self.fields['last_name'].widget.attrs.update({
                # 'id':"form3Example3",
                'class':'form-control form-control-lg',
                'placeholder':'Enter last name'
            })
            self.fields['email'].widget.attrs.update({
                # 'id':"form3Example3",
                'class':'form-control form-control-lg',
                'placeholder':'Enter your Email'
            })
            self.fields['password1'].widget.attrs.update({
                #  'id':"form3Example4",
                'class':'form-control form-control-lg',
                'placeholder':'Enter your password'
            })
            self.fields['password2'].widget.attrs.update({
                # 'id':"form3Example4",
                'class':'form-control form-control-lg',
                'placeholder':'Confirm password'
            })

        first_name = forms.CharField(max_length=50)
        last_name = forms.CharField(max_length=50)
        email = forms.EmailField(max_length=50)
        password1 = forms.CharField(widget=forms.PasswordInput())
        password2 = forms.CharField(widget=forms.PasswordInput())
        class Meta:
            model = User
            fields = ['first_name','last_name', 'email', 'password1', 'password2']

