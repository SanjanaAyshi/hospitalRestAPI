# Generated by Django 5.0.1 on 2024-01-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services/images/'),
        ),
    ]
