# Generated by Django 3.0.4 on 2020-05-17 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Address')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/%Y/%m/%d/', verbose_name='Profile Image')),
                ('join_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Joined Date')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
