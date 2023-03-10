# Generated by Django 4.1.7 on 2023-03-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='delivered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_photo',
            field=models.ImageField(blank=True, null=True, upload_to='job/delivery_photos/'),
        ),
        migrations.AddField(
            model_name='job',
            name='pickedup_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_photo',
            field=models.ImageField(blank=True, null=True, upload_to='job/pickup_photos/'),
        ),
    ]
