from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import VistaLoginCustom


urlpatterns = [
    path('', views.index, name='todolist'),
    path('login', VistaLoginCustom.as_view(), name='login'),
]