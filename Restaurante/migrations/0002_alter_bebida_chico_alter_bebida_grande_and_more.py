# Generated by Django 4.0.3 on 2022-04-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='chico',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='bebida',
            name='grande',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='comida',
            name='chico',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='comida',
            name='grande',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='chica',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='grande',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='reservada',
            field=models.BooleanField(null=True),
        ),
    ]