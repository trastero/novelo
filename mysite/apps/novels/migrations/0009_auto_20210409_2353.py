# Generated by Django 3.2 on 2021-04-09 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('novels', '0008_auto_20210409_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='illustration',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de subida'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.SmallIntegerField(verbose_name='nº'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='volume_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter_volume', to='novels.volume', verbose_name='Volumen'),
        ),
        migrations.AlterField(
            model_name='illustration',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='illustration_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='illustration',
            name='volume_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='illustration_volume', to='novels.volume'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Última actualización'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='novel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volume_novel', to='novels.novel', verbose_name='Novela'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='number',
            field=models.SmallIntegerField(verbose_name='nº'),
        ),
    ]