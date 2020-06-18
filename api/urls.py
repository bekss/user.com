from django.urls import path,include
from .views import ManAPIView,NumberAPI


urlpatterns = [
    path('', ManAPIView.as_view()),
    path('<int:number>/', NumberAPI.as_view(), name='number'),
]