# Generated by Django 4.0.1 on 2022-01-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_device_price_customer_p2p_device_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='closer_box',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='ftth_fiber_length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='ftth_router_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='patch_cord',
            field=models.IntegerField(default=0),
        ),
    ]
