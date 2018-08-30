# Generated by Django 2.0.5 on 2018-08-09 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0009_auto_20180803_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]