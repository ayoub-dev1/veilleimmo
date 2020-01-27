from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, get_user_model
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.mixins import  LoginRequiredMixin


# import generic view 
from  django.views.generic import  DetailView, FormView, View, UpdateView,CreateView
from django.views.generic.edit import FormMixin
from django.utils.http import  is_safe_url
from django.utils.safestring import mark_safe
from .forms import UserLoginForm, UserCreationForm

from django.contrib.messages.views import SuccessMessageMixin

from immobilier.mixins import NextUrlMixin, RequestFormAttachMixin




class AccountHomeView(LoginRequiredMixin, DetailView):
	template_name = 'accounts/home.html'
	def get_object(self):
		return self.request.user


class LoginView(NextUrlMixin,RequestFormAttachMixin,FormView):
 
	form_class = UserLoginForm
	success_url = '/'
	template_name = 'accounts/login.html'
	default_next = '/'

	def form_valid(self, form):
		next_path = self.get_next_url()
		return redirect(next_path)

	# def get_form_kwargs(self):
	# 	kwargs = super(LoginView, self).get_form_kwargs()
	# 	kwargs['request'] = self.request
	# 	return kwargs
    


class RegisterPromoreurView(SuccessMessageMixin,CreateView):
	form_class = UserCreationForm
	template_name = 'accounts/register.html'
	success_url = '/login/'
	success_message = 'You have successfully registered Check Your email '