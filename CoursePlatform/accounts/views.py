from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import FullUserCreationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group,User
from .decorators import unauthenticated
from .models import User
from course.models import Course, CourseContent, Enroll
from django.http import HttpResponse


class HomeView(View):
    """
    Homepage view, default view of the website
    get() retrieves existing objects in our database for the automatic counter of students, partners, courses, enrolled
    """
    template_name = "accounts/homepage.html"
    def get(self, request, *args, **kwargs):

        queryset = Course.objects.all()
        partner = User.objects.filter(is_partner=True).count()
        student = User.objects.filter(is_student=True).count()
        course = queryset.count()
        enroll = Enroll.objects.all().count()
        context = {
            'data': queryset,
            'partner': partner,
            'student': student,
            'course': course,
            'enroll': enroll,
        }
        return render(request, self.template_name, context)


@method_decorator(unauthenticated, name='dispatch')
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
            user = form.save()
            user_type = request.POST.get('user_type')
            if user_type == "1":
                User.objects.filter(pk=user.pk).update(is_student=True)
                group = Group.objects.get(name='Students')
            elif user_type == "2":
                User.objects.filter(pk=user.pk).update(is_partner=True, is_staff=True)
                group = Group.objects.get(name='Partners')
            user.groups.add(group)
            messages.success(request, f"Your account has been successfully created")
            return redirect("login")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class AccountUpdateView(TemplateView):
    """
    Profile update page of each user. Login is required to see this page
    """
    profile_form_class = ProfileUpdateForm
    user_form_class = UserUpdateForm
    template_name = "accounts/profileupdate.html"

    def get(self, request, *args, **kwargs):
        profile_form = self.profile_form_class(instance=request.user.profile)
        user_form = self.user_form_class(instance=request.user)
        purchased_course = Course.objects.filter(enroll__user=request.user)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'purchased_course': purchased_course
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        profile_form = self.profile_form_class(request.POST, request.FILES, instance=request.user.profile)
        user_form = self.user_form_class(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('account_update')
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


@method_decorator(login_required, name='dispatch')
class AccountDashboardView(TemplateView):
    """
    Profile dashboard page of each user. Login is required to see this page
    """
    template_name = "accounts/dashboard.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        context = {'user': user}
        return render(request, self.template_name, context)
