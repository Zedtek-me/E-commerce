# Generated by Django 4.0.3 on 2022-04-11 16:48

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Ebackend', '0002_product_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Ebackend.product')),
            ],
            managers=[
                ('productType', django.db.models.manager.Manager()),
            ],
        ),
    ]
