# Generated by Django 5.1.3 on 2024-11-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxapp', '0008_alter_cart_myid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='myid',
            field=models.IntegerField(max_length=100),
        ),
    ]
