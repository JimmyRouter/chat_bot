# Generated by Django 4.2.4 on 2023-09-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIsite', '0012_remove_payments_invid'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='is_guest_chat',
            field=models.BooleanField(default=True),
        ),
    ]
