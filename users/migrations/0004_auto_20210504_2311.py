# Generated by Django 3.1.7 on 2021-05-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210504_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_joined',
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
