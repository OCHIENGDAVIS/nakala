# Generated by Django 3.1 on 2020-08-13 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0005_citizenmodel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizenmodel',
            name='order_by',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
