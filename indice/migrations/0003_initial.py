# Generated by Django 4.0.3 on 2022-04-18 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('indice', '0002_delete_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=40, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]