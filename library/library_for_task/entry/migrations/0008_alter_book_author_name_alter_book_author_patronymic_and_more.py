# Generated by Django 4.2.5 on 2023-09-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0007_alter_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_patronymic',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_surname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
