# Generated by Django 4.0.3 on 2022-05-31 02:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0005_alter_comida_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comida',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 2, 1, 49, 605155, tzinfo=utc)),
        ),
    ]
