from django.shortcuts import render, redirect
from entry import models
from .models import Register
from datetime import datetime


def home(request, pk):
    user = models.Lib_User.objects.get(id=pk)
    reg = Register.objects.all()
    context = {
        'reg': reg,
        'user': user,
    }
    return render(request, 'home_app/home_page.html', context)


def check_dict(request, user_pk):
    user = models.Lib_User.objects.get(id=user_pk)
    reg = Register.objects.all()
    context = {
        'register': reg,
        'user': user,
    }
    return render(request, 'home_app/check_dict.html', context)


def books(request, user_pk):
    admin = models.Lib_User.objects.get(name='admin').id
    library_books = models.Book.objects.all().filter(user=admin).order_by('author_surname')
    user = models.Lib_User.objects.get(id=user_pk)

    context = {
        'books': library_books,
        'user_pk': user_pk,
        'user': user
    }
    return render(request, 'home_app/books_list.html', context)


def user_books(request, user_pk):
    books = models.Book.objects.all().filter(user=user_pk).order_by('author_surname')

    context = {
        'books': books,
        'user_pk': user_pk
    }
    return render(request, 'home_app/user_books.html', context)


def all_users_books(request, user_id):
    admin = models.Lib_User.objects.get(name='admin')
    users_books = models.Book.objects.all().exclude(user=admin)

    context = {
        'user_id': user_id,
        'books': users_books,
    }
    return render(request, 'home_app/all_users_books.html', context)


def book_take(request):
    if request.method == 'POST':

        book_id = request.POST['book_number']
        user_id = request.POST['user_id']

        admin = models.Lib_User.objects.get(name='admin').id
        user = models.Lib_User.objects.get(id=user_id)

        take_date = datetime.now()

        try:
            book = models.Book.objects.filter(user=admin).get(id=book_id)
            book.user = user
            book.save()

            register = Register(user_name=user.name, user_surname=user.surname, book_name=book.book_name,
                                user_id=user_id, book_id=book_id, date_take=take_date)
            register.save()
            return redirect('entry_page')
        except:
            return redirect('exception')

    # cart = Cart(request)
    # product = get_object_or_404(Event, id=product_id)
    # cart.remove(product)


def book_return(request):
    if request.method == 'POST':

        book_id = request.POST['book_number']
        user_id = request.POST['user_id']
        admin = models.Lib_User.objects.get(name='admin')
        return_date = datetime.now()

        try:
            book = models.Book.objects.filter(user=user_id).get(id=book_id)
            book.user = admin
            book.save()

            register = Register.objects.filter(user_id=user_id, book_id=book_id).last()
            register.date_return = return_date
            register.save()
            return redirect('entry_page')
        except:
            return redirect('exception')


def exception(request):
    return render(request, 'home_app/except_page.html')
