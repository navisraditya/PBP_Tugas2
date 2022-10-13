from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, add_list_todo, show_json, views_ajax, add_task_ajax, delete_task, change_status

app_name='todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('html/', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addtodolist/', add_list_todo, name='add_todolist'),
    path('views_int_json/', show_json, name='show_json'),
    path('json/', views_ajax, name='views_ajax'),
    path('add/', add_task_ajax, name='add_task_ajax'),
    path('delete_todolist', delete_task, name='delete_task'),
    path('change_status/', change_status, name='change_status'),
]