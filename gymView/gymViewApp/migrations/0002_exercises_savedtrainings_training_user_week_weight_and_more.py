# Generated by Django 4.2.7 on 2023-11-18 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymViewApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavedTrainings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('exercises', models.ManyToManyField(to='gymViewApp.exercises')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Trening', max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True, null=True)),
                ('exercises', models.ManyToManyField(to='gymViewApp.exercises')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('nick', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('number_of_series', models.IntegerField()),
                ('number_of_replication', models.IntegerField()),
                ('weight', models.FloatField()),
                ('comment', models.TextField()),
                ('exercises', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.exercises')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255)),
                ('weight', models.FloatField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Muzyk',
        ),
        migrations.AddField(
            model_name='training',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.user'),
        ),
        migrations.AddField(
            model_name='savedtrainings',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.user'),
        ),
        migrations.AddField(
            model_name='exercises',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.user'),
        ),
        migrations.AddField(
            model_name='exercises',
            name='weeks',
            field=models.ManyToManyField(related_name='exercise_weeks', to='gymViewApp.week'),
        ),
    ]
