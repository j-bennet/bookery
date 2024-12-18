# Generated by Django 5.1.2 on 2024-10-14 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('category', models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Fantasy', 'Fantasy'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Cookbook', 'Cookbook'), ('Science', 'Science'), ('Children', 'Children'), ('Other', 'Other')], max_length=100)),
                ('language', models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('ru', 'Russian')], max_length=100)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
