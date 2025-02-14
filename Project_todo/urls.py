from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home_view, name='home_view'),
    path('delete/<int:todo_id>/', views.delete_view, name='delete_view'),
]
