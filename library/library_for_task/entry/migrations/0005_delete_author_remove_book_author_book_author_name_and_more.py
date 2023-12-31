# Generated by Django 4.2.5 on 2023-09-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0004_alter_book_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='author_patronymic',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='author_surname',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
