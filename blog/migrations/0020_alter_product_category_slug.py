# Generated by Django 3.2 on 2021-05-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_product_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_slug',
            field=models.CharField(default='', editable=False, max_length=25),
        ),
    ]
