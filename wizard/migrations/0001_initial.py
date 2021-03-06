# Generated by Django 3.1.3 on 2020-11-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=200, verbose_name='Ilość')),
                ('price', models.FloatField(default=0, verbose_name='Cena')),
                ('width', models.FloatField(default=0, verbose_name='Szerokość')),
                ('height', models.FloatField(default=0, verbose_name='Wysokość')),
                ('length', models.FloatField(default=0, verbose_name='Długość')),
                ('material', models.CharField(choices=[
                 ('black', 'czarny'), ('transparent', 'przezroczysty')], max_length=128)),
                ('product_type', models.CharField(choices=[
                 ('mailerbox', 'MailerBox'), ('polymailer', 'PolyMailer')], max_length=128)),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('created', 'utworzona'), (
                    'accepted', 'zaackeptowana'), ('rejected', 'odrzucona')], max_length=128)),
                ('products', models.ManyToManyField(
                    blank=True, to='wizard.Product')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Oferty',
            },
        ),
    ]
