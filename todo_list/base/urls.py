from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import LoginViewTodoList, profile, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, StatusChange


urlpatterns = [
    path('', views.index, name='todolist'),
    path('login/', LoginViewTodoList.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='todolist'), name='logout'),
    path('profile/', profile.as_view(), name='profile'),
    path('profile/task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-complete/', StatusChange.as_view(), name='task-complete'),
]