
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.book_list),
    path('book/<slug:slug>/', views.book_detail),
    path('book/<slug:slug>/add', views.book_add),
    path('book/<slug:slug>/delete', views.book_delete),
    path('book/<slug:slug>/edit', views.book_edit),
    path('admin/', admin.site.urls),
]
