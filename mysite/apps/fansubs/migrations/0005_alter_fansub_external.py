# Generated by Django 3.2 on 2021-04-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fansubs', '0004_alter_fansub_external'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fansub',
            name='external',
            field=models.JSONField(default='', null=True),
        ),
    ]