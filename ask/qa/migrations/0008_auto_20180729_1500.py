# Generated by Django 2.0.5 on 2018-07-29 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0007_auto_20180729_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='name',
            new_name='email',
        ),
    ]
