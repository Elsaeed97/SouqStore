# Generated by Django 3.0.4 on 2020-05-17 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200509_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATImg',
            field=models.ImageField(upload_to='category/%Y/%m/%d/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDISBestseller',
            field=models.BooleanField(default=False, verbose_name='BestSeller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=True, verbose_name='New Product ?'),
        ),
    ]
