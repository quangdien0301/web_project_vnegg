from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import TemplateView, FormView


class SiteLoginView(LoginView):
    template_name = 'login.html'

class RegisterForm(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username",'email')
        field_classes = {'username': UsernameField}
        widgets = {
            'email': forms.EmailInput(attrs={'required':True})
        }




class SiteRegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(username=data['username'],
                                            password=data['password1'],
                                            email=data['email']
                                            )
        url = f"{reverse('register_ok')}?username={new_user.username}"
        from pprint import pprint
        print(url)
        return redirect(url)


class SiteRegisterOkView(TemplateView):
    template_name = 'register_ok.html'



class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'