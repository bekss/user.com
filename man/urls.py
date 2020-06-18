from django.urls import path
from man import views
from man.views import Users, ShowUsers,User,create_user

urlpatterns = [
    path('',views.login, name='login'),
    path('man/',views.registr, name='man'),
    path('users/<int:number>/',Users.as_view(), name='users'),
    path('logout/', views.logout, name='logout'),
    path('showusers/', ShowUsers.as_view(), name='showusers'),
    path('api/users', views.create_user, name='user'),

]

