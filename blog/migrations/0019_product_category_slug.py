# Generated by Django 3.2 on 2021-05-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]