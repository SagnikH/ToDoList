from django.urls import path

from . import views

app_name = 'records'

urlpatterns = [
    # path('', views.RecordListView.as_view(), name='todoList'),
    path('', views.recordListView, name='todoList'),
    path('delete/<int:pk>', views.RecordDeleteView.as_view(), name='delete'),
    path('create/', views.RecordCreateView.as_view(), name='create'),
]