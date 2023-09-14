from django.shortcuts import render, redirect
from .models import Lib_User
from .forms import CreateLibUser, CreateBook


def entry_page(request):
    users = Lib_User.objects.all().order_by('surname')
    context = {
        "users": users
    }

    return render(request, 'entry/entry_page.html', context)


def registration(request):
    form = CreateLibUser

    if request.method == 'POST':
        form = CreateLibUser(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['name']
            user_surname = form.cleaned_data['surname']
            try:
                user = Lib_User.objects.filter(name=user_name, surname=user_surname)
                return redirect('exception')
            except:
                form.save()
                return redirect('entry_page')

    context = {
        'form': form,
    }

    return render(request, 'entry/registration.html', context)


def creation(request):
    form = CreateBook

    if request.method == 'POST':
        form = CreateBook(request.POST)

        if form.is_valid():
            form.save()
            return redirect('entry_page')

    context = {
        'form': form,
    }

    return render(request, 'entry/book_creation.html', context)
