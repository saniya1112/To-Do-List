from django.contrib import admin
from django.urls import path
from .import views
from .views import*
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing, name='landing'),
    path('home/', views.home, name = 'home'),
    path('all_task/',views.all_task, name = 'all_tasks'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('todo/', todo_list, name='todo_list'),
    path('add_task/',add_task, name='add_task'),
    path('complete_task/', complete_task, name='complete_task'),
    path('delete_task/<int:task_id>', delete_task, name='delete_task'),
    path('profile/', profile, name='profile'),
    path('custom_logout/', custom_logout, name='logout'),
    path('complete_task/<int:task_id>/', complete_task, name='complete_task'),
    path('reassign_task/<int:task_id>/', reassign_task, name='reassign_task'),


]