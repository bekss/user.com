from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render_to_response, render
from django.core.exceptions import PermissionDenied
from django.urls import reverse


def dont_user(view_func):
    def next_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('man')
        else:
            return view_func(request, *args, **kwargs)
    return next_func


def access_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                # sendd='доступ запрещен'
                # return render(request,'log/login.html',{'sendd':sendd})
                return redirect('login')
        return wrapper_func
    return decorator



# def access_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             if request.user.is_staff:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return render_to_response('NotFound.html')
#
#         return wrapper_func
#
#     return decorator

