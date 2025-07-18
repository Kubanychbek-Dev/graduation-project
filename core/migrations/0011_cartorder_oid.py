# Generated by Django 5.0.14 on 2025-07-10 13:59

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_cartorder_order_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='oid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcde123456', length=10, max_length=20, prefix='ord', unique=True),
        ),
    ]
