from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.home, name='home_page'),
    path('books<int:user_pk>/', views.books, name='books'),
    path('user_books<int:user_pk>/', views.user_books, name='user_books'),
    path('check_dict<int:user_pk>/', views.check_dict, name='check_dict'),
    path('book_take/', views.book_take, name='book_take'),
    path('book_return/', views.book_return, name='book_return'),
    path('exception/', views.exception, name='exception'),
    path('all_users_books<int:user_id>/', views.all_users_books, name='all_users_books'),
]
