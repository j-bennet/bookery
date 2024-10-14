# Generated by Django 5.1.2 on 2024-10-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Fantasy', 'Fantasy'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Cookbook', 'Cookbook'), ('Science', 'Science'), ('Children', 'Children'), ('Other', 'Other')], default='Fiction', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('ru', 'Russian')], default='en', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]