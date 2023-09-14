from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.entry_page, name='entry_page'),
    path('registration/', views.registration, name='registration'),
    path('create_book/', views.creation, name='creation'),
    path('home/', include('home.urls'), name='home_page')
]