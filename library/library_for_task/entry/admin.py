from django.contrib import admin
from .models import Lib_User, Book
# register the purchase model to see it in the admin panel

admin.site.register(Lib_User)
admin.site.register(Book)
