# Generated by Django 4.2.7 on 2023-11-21 15:14

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SavedTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Trening', max_length=255)),
                ('date', models.DateField()),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nick', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(default='New_User', max_length=150, unique=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='gymviewapp_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='gymviewapp_user_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weight', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('number_of_series', models.IntegerField()),
                ('number_of_replication', models.IntegerField()),
                ('weight', models.FloatField()),
                ('comment', models.TextField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_series', models.IntegerField()),
                ('number_of_replication', models.IntegerField()),
                ('weight', models.FloatField()),
                ('comment', models.TextField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.exercise')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.training')),
            ],
        ),
        migrations.AddField(
            model_name='training',
            name='exercises',
            field=models.ManyToManyField(through='gymViewApp.TrainingExercise', to='gymViewApp.exercise'),
        ),
        migrations.AddField(
            model_name='training',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.user'),
        ),
        migrations.CreateModel(
            name='SavedTrainingExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.exercise')),
                ('saved_training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.savedtraining')),
            ],
        ),
        migrations.AddField(
            model_name='savedtraining',
            name='exercises',
            field=models.ManyToManyField(through='gymViewApp.SavedTrainingExercise', to='gymViewApp.exercise'),
        ),
        migrations.AddField(
            model_name='savedtraining',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymViewApp.user'),
        ),
    ]