# Generated by Django 3.2 on 2021-07-17 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BICON_App', '0003_branches_cutoff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='Category_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rounds',
            name='Round',
            field=models.CharField(default='', max_length=10),
        ),
    ]
