# Generated by Django 4.0.3 on 2022-03-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ebackend', '0002_rename_buyer_buyerprofile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0, max_length=10),
        ),
    ]
