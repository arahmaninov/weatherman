from django.urls import path

from . import views


app_name = 'user'

urlpatterns = [
        path('', views.show_main, name='main')
]
