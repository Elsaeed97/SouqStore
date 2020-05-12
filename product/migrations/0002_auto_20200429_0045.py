# Generated by Django 3.0.4 on 2020-04-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDImage_1',
            field=models.ImageField(default=1, upload_to='products/%Y/%m/%d/', verbose_name='Product Main Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='PRDImage_2',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/', verbose_name='ProductImage 2'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDImage_3',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/', verbose_name='ProductImage 3'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDImage_4',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/', verbose_name='ProductImage 4'),
        ),
    ]