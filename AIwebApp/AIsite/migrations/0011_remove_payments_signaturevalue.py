# Generated by Django 4.2.4 on 2023-09-15 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AIsite', '0010_product_token_limit_alter_product_product_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='SignatureValue',
        ),
    ]
