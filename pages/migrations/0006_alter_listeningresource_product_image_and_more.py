# Generated by Django 4.2.6 on 2023-10-07 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_listeningresource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listeningresource',
            name='product_image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='listeningresource',
            name='url',
            field=models.TextField(),
        ),
    ]
