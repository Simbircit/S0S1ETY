# Generated by Django 5.1.6 on 2025-02-28 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='Жуймайсынба.png', upload_to='images'),
        ),
    ]
