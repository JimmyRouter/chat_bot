# Generated by Django 4.2.4 on 2023-09-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIsite', '0004_alter_payments_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_ips', models.JSONField()),
                ('guest_session', models.CharField(max_length=1024)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=1000, max_digits=8, null=True)),
            ],
        ),
    ]
