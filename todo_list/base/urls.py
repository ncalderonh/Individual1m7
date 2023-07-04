from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import LoginViewTodoList, profile, TaskDetail, TaskCreate


urlpatterns = [
    path('', views.index, name='todolist'),
    path('login/', LoginViewTodoList.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='todolist'), name='logout'),
    path('profile/', profile.as_view(), name='profile'),
    path('profile/task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
]