# Generated by Django 4.2.7 on 2023-11-20 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymViewApp', '0003_remove_weight_user_weight_exercises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='week',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='weight',
            name='date',
            field=models.DateField(),
        ),
    ]