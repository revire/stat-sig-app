# Generated by Django 2.2.5 on 2020-02-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_datafile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafile',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]