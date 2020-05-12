# Generated by Django 3.0.4 on 2020-04-29 00:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATName', models.CharField(max_length=80, verbose_name='Category Name')),
                ('CATDesc', models.TextField(verbose_name='Description')),
                ('CATImg', models.ImageField(upload_to='category/%Y/%m/%d/', verbose_name='Category Image')),
                ('CATParent', models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Parent Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=100, verbose_name='Product Name')),
                ('PRDDesc', models.TextField(verbose_name='Description')),
                ('PRDPrice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('PRDCost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost')),
                ('PRDCreated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]