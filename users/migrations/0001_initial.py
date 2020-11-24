# Generated by Django 3.1.3 on 2020-11-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254,
                                            unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True,
                                                max_length=32, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                                               max_length=128, verbose_name='last name')),
                ('is_active', models.BooleanField(
                    default=False, verbose_name='active')),
                ('user_type', models.CharField(choices=[('client', 'klient'), ('salesman', 'sprzedawca'), (
                    'superuser', 'administrator')], default='client', max_length=16, verbose_name='typ')),
            ],
            options={
                'verbose_name': 'Użytkownik',
                'verbose_name_plural': 'Użytkownicy',
            },
        ),
    ]