# Generated by Django 3.1.3 on 2022-06-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0004_auto_20220607_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='current_user',
            name='voted_position_5',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='current_user',
            name='voted_position_6',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='current_user',
            name='voted_position_7',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
