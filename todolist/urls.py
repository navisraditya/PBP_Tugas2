from django.urls import path
from Lab01.wishlist.views import show_json_by_id
from todolist.views import show_todolist, register, login_user, logout_user, add_list_todo, show_json, show_json_by_id

app_name='todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('html/', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addtodolist/', add_list_todo, name='add_todolist'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]