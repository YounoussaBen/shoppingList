# Generated by Django 4.0.6 on 2022-09-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2000)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
