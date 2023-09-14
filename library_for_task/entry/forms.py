from django import forms
from .models import Lib_User, Book


class CreateLibUser(forms.ModelForm):
    class Meta:
        model = Lib_User
        fields = ['name', 'surname', 'patronymic']


class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author_name', 'author_surname', 'author_patronymic']
