# Generated by Django 3.2.4 on 2021-06-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='historicalcar',
            name='id',
            field=models.IntegerField(blank=True, db_index=True),
        ),
    ]
