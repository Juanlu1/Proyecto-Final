# Generated by Django 4.0.3 on 2022-05-30 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indice', '0005_remove_userinfo_descripcion_remove_userinfo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='descripcion',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='link',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
