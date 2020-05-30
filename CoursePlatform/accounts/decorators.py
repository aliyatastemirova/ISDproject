from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view_function):
    """
    A decorator that checks if the user is logged in
    Either redirects the user to their account or lets them proceed with the requested function
    Used for methods that should only be accessed by unauthenticated users
    :param view_function: the function that uses this decorator in views.py
    :return: if authenticated: account page, else calls the view function
    """

    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function
