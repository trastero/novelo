# Generated by Django 3.2 on 2021-04-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='artist',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='novel',
            name='author',
            field=models.JSONField(null=True),
        ),
    ]