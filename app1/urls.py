from django.urls import path
from app1.views import *

urlpatterns = [
    path('',index,name='home'),
    path('loginuser',loginuser,name='loginuser'),
    path('todo',todo_list,name='todo'),
    path('logoutuser',logoutuser,name='logout'),
    path('add_task',add_task,name='all_task'),
    path('signinuser',signinuser,name='signin'),
    path('delete/<int:id>/',delete_item,name='delete_item'),
    path('edit/<int:id>/',edit_item,name='edit_item'),
    path('complete/<int:id>/',add_to_complete,name='complete')
]
