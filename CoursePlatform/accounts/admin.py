from django.contrib import admin
from .models import User, Profile
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from django import forms


class GroupAdminForm(forms.ModelForm):
    """
    ModelForm that adds an additional multiple select field for managing
    the users in the group. We can easily see which users belong to a group and make modifications
    """
    users = forms.ModelMultipleChoiceField(
        User.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('Users', False),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            initial_users = self.instance.user_set.values_list('pk', flat=True)
            self.initial['users'] = initial_users

    def save(self, *args, **kwargs):
        kwargs['commit'] = True
        return super(GroupAdminForm, self).save(*args, **kwargs)

    def save_m2m(self):
        self.instance.user_set.clear()
        self.instance.user_set.add(*self.cleaned_data['users'])


class NewGroupAdmin(GroupAdmin):
    """
    Customized GroupAdmin class that uses the customized form to allow user management within a group.
    """
    form = GroupAdminForm
    list_display = ["name", "pk"]


class UserTypeFilter(SimpleListFilter):
    """
    Allows filtering users by their type (student or partner)
    """
    title = 'User type'
    parameter_name = 'user_type'

    def lookups(self, request, model_admin):
        """
        We have two filter options
        :return: a list of tuples with filter options
        """
        return [
            ('is_student', 'Student'),
            ('is_partner', 'Partner'),
        ]

    def queryset(self, request, queryset):
        """
        Filters by selected options
        """
        # Filter by selected options
        if self.value() == 'is_student':
            return queryset.distinct().filter(is_student=True)
        if self.value() == 'is_partner':
            return queryset.distinct().filter(is_partner=True)


class UserAdmin(admin.ModelAdmin):
    """
    Admin class for Users, allows to use the custom user type filter and to display all attributes in the admin panel
    """
    # Add the option to filter by user type
    list_filter = [UserTypeFilter]
    # Display all fields in admin panel
    list_display = ['id', 'username', 'email', 'is_student', 'is_partner']


class ProfileAdmin(admin.ModelAdmin):
    """
    Admin class for Profiles, allows to display all attributes in the Django admin panel
    """
    list_display = ['id', 'first_name', 'last_name', 'gender', 'birth_date', 'country']


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
# Group is already registered with auth.GroupAdmin, so we need to unregister it first
admin.site.unregister(Group)
# And register again with the custom GroupAdmin
admin.site.register(Group, NewGroupAdmin)
