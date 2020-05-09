from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view_function):

    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function