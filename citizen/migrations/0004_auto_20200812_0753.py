# Generated by Django 3.1 on 2020-08-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0003_auto_20200812_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizenmodel',
            name='checksum',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='citizenmodel',
            name='path',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='citizenmodel',
            name='status',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]