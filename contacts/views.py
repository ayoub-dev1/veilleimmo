from django.shortcuts import render
from django.views.generic import  CreateView
from .forms import  ContactForm



class SendContactForm(CreateView):
    form_class  = ContactForm
    template_name = 'contact/contact.html'
    success_url = '/'
