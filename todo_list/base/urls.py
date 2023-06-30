from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import LoginViewTodoList, profile


urlpatterns = [
    path('', views.index, name='todolist'),
    path('login/', LoginViewTodoList.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='todolist'), name='logout'),
    path('profile/', profile, name='profile'),
]