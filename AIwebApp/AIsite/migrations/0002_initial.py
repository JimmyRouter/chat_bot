# Generated by Django 4.2.4 on 2023-08-31 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AIsite', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='data_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userdata',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='AIsite.product'),
        ),
        migrations.AddField(
            model_name='payments',
            name='expiration_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expiration_period', to='AIsite.duration'),
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_owner', to='AIsite.userdata'),
        ),
        migrations.AddField(
            model_name='payments',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AIsite.product'),
        ),
        migrations.AddField(
            model_name='messages',
            name='parent_chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='AIsite.chat'),
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatuser', to='AIsite.userdata'),
        ),
    ]
