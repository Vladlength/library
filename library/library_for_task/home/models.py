from django.db import models


class Register(models.Model):
    user_id = models.CharField(max_length=60, null=True, blank=True)
    user_name = models.CharField(max_length=60, null=True, blank=True)
    user_surname = models.CharField(max_length=60, null=True, blank=True)
    book_name = models.CharField(max_length=60, null=True, blank=True)
    book_id = models.CharField(max_length=60, null=True, blank=True)
    date_take = models.DateField(null=True, blank=True)
    date_return = models.DateField(null=True, blank=True)
