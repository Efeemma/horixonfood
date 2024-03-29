# Generated by Django 4.2.5 on 2023-09-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0005_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]
