from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model, authenticate, login
from django.core.validators import RegexValidator
from django.db.models import Q
from django.contrib import  messages
from .models import User

User = get_user_model()


''' Login Form '''
class UserLoginForm(forms.Form):
    query    = forms.CharField(label="username/email", widget=forms.TextInput(attrs={"class": 'form-control simple'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={"class":"form-control simple"}))

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(UserLoginForm, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        request = self.request
        data = self.cleaned_data
        query         = data.get('query')
        password      = data.get('password')
        # check if email or username are exists
        user_qs_final = User.objects.filter(
            Q(username__iexact=query) |
            Q(email__iexact=query)
        ).distinct() # get just one : email or email not both

        # check if user is exist and user should be one user
        if not user_qs_final.exists() and user_qs_final.count() != 1:
            raise forms.ValidationError('Invalide username')
        user_obj = user_qs_final.first() # get the unique user
        # check password of the existing user
        if not user_obj.check_password(password):
            raise forms.ValidationError('Invalid password')
        # check if is active
        if not user_obj.is_active:
            raise forms.ValidationError('Inactive User! please verify your email address')
        user = authenticate(request, username=query, password=password)
        if user is None:
            messages.warning(request,"Invalid credentials")
            raise forms.ValidationError('invalid credentials')
        login(request,user)
        messages.warning(request, 'You have been successfully  logged in' + user.email)
        self.user = user
        return data
        

''' User Creation Form '''

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control simple'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control simple'}))

    class Meta:
        model = User
        fields = ('username', 'email','full_name')

        widgets = {
            'email':forms.TextInput(attrs={"class":'form-control simple', 'type':'email'}),
            'full_name':forms.TextInput(attrs={"class":'form-control simple', 'type':'text'}),
            'username':forms.TextInput(attrs={"class":'form-control simple', 'type':'text'}),
            # 'is_promoteur':forms.CheckboxInput(attrs={"class":'form-control simple'}),
            # 'site_web':forms.TextInput(attrs={"class":'form-control simple', 'type':'text'}),
            # 'adresse_siege_social':forms.Textarea(attrs={"class":'form-control simple', 'type':'text'}),
            
        }
    
    def clean_password2(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords dont Match ')
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.is_active = False
        if commit:
            user.save()
        return user
    
    


class UserCreationFormPromoteur(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control simple'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control simple'}))
    site_web  = forms.CharField(label='Site web ', widget=forms.TextInput(attrs={'class':'form-control simple'}))
    adresse_siege_social = forms.CharField(label='address', widget=forms.Textarea(attrs={'class':'form-control simple'}))
    class Meta:
        model = User
        fields = ('username', 'email','full_name', 'is_promoteur')

        widgets = {
            'email':forms.TextInput(attrs={"class":'form-control simple', 'type':'email'}),
            'full_name':forms.TextInput(attrs={"class":'form-control simple', 'type':'text'}),
            'username':forms.TextInput(attrs={"class":'form-control simple', 'type':'text'}),
            'is_promoteur':forms.CheckboxInput(attrs={"class":'form-control simple'}),
            'site_web':forms.TextInput(attrs={"class":'form-control simple', 'type':'text'}),
            'adresse_siege_social':forms.Textarea(attrs={"class":'form-control simple', 'type':'text'}),
            
        }
    
    def clean_password2(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords dont Match ')
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.is_active = False
        if commit:
            user.save()
        return user
    
    



''' User Change Form '''

class ChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model  = User
        fields = ('username', 'email', 'password', 'is_staff','is_active', 'is_admin')

        def clean_password(self):
            return self.initial['password']