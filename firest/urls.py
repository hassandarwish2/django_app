"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    crispy forms
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from tracks_jogging import views



urlpatterns = [
    path('admin/', admin.site.urls),


    path('signup/', views.SignupView.as_view(), name='signup'),
    path('',views.MyLogin.as_view(), name='login'),
    path('logout/',views.signout, name='logout'),
    path('mylist/', views.MyLists.as_view(), name='mylist'),

    path('ls_list_week', views.trackweek, name='filterbyweek'),
    path('ls_list_month', views.trackmonth, name='filterbymonth'),
    path('mylists/', views.MyLists.as_view(), name='mylists'),

    path('my-lists/<int:pk>/update', views.TodoListUpdateView.as_view(), name='list-update'),
    path('my-lists/add/', views.AddTodoListView.as_view(), name='add-list'),
    path('my-lists/<int:pk>/delete', views.DeleteTodoListView.as_view(), name='list-delete'),
]