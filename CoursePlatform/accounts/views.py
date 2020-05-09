from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import FullUserCreationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.models import Group



class HomeView(TemplateView):
    """
    Homepage view, default view of the website
    """
    template_name = "accounts/homepage.html"



class RegistrationFormView(FormView):
    
    form_class = FullUserCreationForm
    template_name = "accounts/register.html"
    success_url = '/register/'  

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def form_valid(self,form):

        partnerId=Group.objects.filter(name="Partner").values_list('id',flat=True)
           
        user = User()
        user.username=self.request.POST['username']
        user.email=self.request.POST['email']
        if self.request.POST['type'] == partnerId:
            user.is_staff=True
        else:
            user.is_staff=False

        user.save()
        user.groups.add(self.request.POST['type'])
        messages.success(self.request, f"Your account has been successfully created")
        return redirect("register")
        
        

    # def post(self, request, *args, **kwargs):
           
    #     registration_form=self.form_class(request.POST)
    #     if registration_form.is_valid:
    #         user = User()
    #         user.username=request.POST['username']
    #         user.email=request.POST['email']
    #         user.save()
    #         user.groups.add(request.POST['type'])
    #         messages.success(request, f"Your account has been successfully created")
    #         return redirect("register")



      


@method_decorator(login_required, name='dispatch')
class AccountView(TemplateView):
    """
    Profile page of each user. Login is required to see this page
    """
    profile_form_class = ProfileUpdateForm
    user_form_class = UserUpdateForm
    template_name = "accounts/profile.html"

    def get(self, request, *args, **kwargs):
        profile_form = self.profile_form_class(instance=request.user.profile)
        user_form = self.user_form_class(instance=request.user)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, self.template_name, context)

   

    def post(self, request, *args, **kwargs):
        profile_form = self.profile_form_class(request.POST, request.FILES, instance=request.user.profile)
        user_form = self.user_form_class(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            messages.success(request, f'Your account has been successfully updated')
            return redirect('account')
        else:
            messages.error(request, 'Please fill out the fields correctly')
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class PasswordChangeView(TemplateView):
    """
    Password change view form on a new page. Login required
    """
    form_class = PasswordChangeForm
    template_name = "accounts/passwordchange.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
        return render(request, self.template_name, {'form': form})
