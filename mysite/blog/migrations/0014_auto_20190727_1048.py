# Generated by Django 2.2.3 on 2019-07-27 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_notification_id_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='id_target',
            field=models.IntegerField(),
        ),
    ]
