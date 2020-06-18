from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .forms import NewMann
from django.contrib.auth.decorators import login_required
from .decorators import dont_user, access_users
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Man
from .serializers import Order, UserRegistration
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from man.serializers import UserRegistration
from rest_framework.views import Response


# @dont_user

@csrf_protect
def login(request):
    send = {}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            send['login_error'] = "Колдонуучу катталган эмес туура маалыматты жазыныз"
            return render(request, 'log /login.html', send)
    else:
        return render(request, 'log/login.html', send)



@access_users(allowed_roles=['beka'])
@csrf_protect
def registr(request):
    send = {}
    if request.method == 'POST':
        form = NewMann(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(username=request.POST['number'], password=request.POST['pin'])
            if user is not None:
                print('valid')
                obj = form.save(commit=False)
                obj.user = user
                obj.save()
                newform = NewMann()
                return render(request, 'registration/registration.html', {'form': newform})
            else:
                send['login_error'] = "Колдонуучу табылган жок туура териниз"
                return render_to_response('registration/registration.html', send)
        else:
            return render(request, 'registration/registration.html', {'form': form})
    else:
        form = NewMann()
        return render(request, 'registration/registration.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('login')


class Users(DetailView):
    model = Man
    template_name = 'users.html'

    def get(self, request, number):
        try:
            person = Man.objects.get(number=number)
            print(person)
            return render(request, 'users.html', {'person': person})
        except self.model.DoesNotExist:
            raise Http404


class ShowUsers(UserPassesTestMixin, ListView):
    login_url = 'login'
    login_required(login_url='login')
    model = Man
    queryset = Man.objects.all()
    template_name = 'showusers.html'

    def test_func(self):
        return self.request.user.is_superuser


class AllUsers(ModelViewSet):
    queryset = Man.objects.all()
    serializer_class = Order


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserRegistration(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            username=request.POST['number'], password=request.POST['pin']
        )
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class Register(viewsets.ModelViewSet):
    queryset = Man.objects.all()
    serializer_class = UserRegistration
