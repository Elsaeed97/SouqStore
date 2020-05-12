# Generated by Django 3.0.4 on 2020-05-09 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_prdslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDDiscountPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Discount Price'),
            preserve_default=False,
        ),
    ]
