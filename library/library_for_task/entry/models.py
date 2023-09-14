from django.db import models


class Lib_User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)

    def __str__(self):
        return str(self.surname)


class Book(models.Model):
    book_name = models.CharField(max_length=60, null=True, blank=True)
    author_name = models.CharField(max_length=20, null=True, blank=True)
    author_surname = models.CharField(max_length=20, null=True, blank=True)
    author_patronymic = models.CharField(max_length=20, null=True, blank=True)
    user = models.ForeignKey(Lib_User, on_delete=models.SET_DEFAULT, default=Lib_User.objects.get(name='admin').id, )

    def __str__(self):
        return str(self.book_name)
