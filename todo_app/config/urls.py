"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from todo.views import index_view, form_save_view, task_edit_view, submit_edit_view, submit_delete_view, delete_view, status_change_view, edit_view, index_json_view, json_frontend_view
from mainpage.views import tasks_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('form-save/', form_save_view, name='form-save'),
    path('tasks/', tasks_view, name='tasks'),
    path('tasks/task-edit/<int:pk>/', task_edit_view, name='task-edit'),
    path('tasks/submit-edit/<int:pk>/', submit_edit_view, name='submit-edit'),
    path('tasks/submit-delete/', submit_delete_view, name = 'submit-delete'),
    path('tasks/delete/', delete_view, name= 'delete'),
    path('tasks/status-change/<int:pk>/', status_change_view, name= 'status-change'),
    path('tasks/edit/', edit_view, name='edit'),
    path('json_simple', index_json_view, name='index-json'),
    path('json_frontend/', json_frontend_view, name='json-frontend'),
]
