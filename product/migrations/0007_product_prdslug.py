# Generated by Django 3.0.4 on 2020-05-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200429_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug'),
        ),
    ]
