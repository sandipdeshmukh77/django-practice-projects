from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movienews/', views.movienews),
    path('sportsnews/', views.sportsnews),
    path('politicsnews/', views.politicsnews),
    path('', views.home),
]
