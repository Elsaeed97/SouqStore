# Generated by Django 3.0.4 on 2020-05-09 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_prddiscountprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDISBestseller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=True),
        ),
    ]
