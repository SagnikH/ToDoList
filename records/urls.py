from django.urls import path

from . import views

urlpatterns = [
    path('', views.recordListView, name='todoList'),
    path('delete/<int:id>', views.deleteView, name='delete'),
]