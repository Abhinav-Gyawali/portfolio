# Generated by Django 4.2.3 on 2023-07-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='reply',
            field=models.TextField(default='error'),
            preserve_default=False,
        ),
    ]
