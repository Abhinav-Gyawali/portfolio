# Generated by Django 4.2.6 on 2023-10-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeningResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('product_image', models.URLField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('url', models.URLField()),
                ('desc', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
