# Generated by Django 3.2.1 on 2021-07-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(max_length=255, null=True, upload_to='', verbose_name='Suba la imagen del producto'),
        ),
    ]
