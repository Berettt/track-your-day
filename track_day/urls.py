from django.urls import path
from .views import *

app_name = 'track_day'

urlpatterns = [
    path('home',home,name='home'),
    path('login/',log_in,name='login'),
    path('register/',reg_ister,name='register'),
    path('day',day,name='day'),
    path('create_day/add_task',add_task,name='addtask'),
    path('create_day/delete_task',delete_task,name='deletetask'),
    path('day/<int:pk>/',id_day,name='pkday')
]