# Generated by Django 3.0.5 on 2020-05-12 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
