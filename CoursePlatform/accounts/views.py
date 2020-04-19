from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import FullUserCreationForm
from django.contrib import messages
from .models import Student


class HomeView(TemplateView):
    """
    Homepage view, default view of the website
    """
    template_name = "accounts/homepage.html"


class RegistrationFormView(View):
    """
    Registration form for new users.
    Necessary fields: username, email, password, repeat password
    """
    form_class = FullUserCreationForm
    template_name = "accounts/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been successfully created")
            return redirect("login")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class AccountView(TemplateView):
    """
    Profile page of each user. Login is required to see this page
    """
    template_name = "accounts/profile.html"

