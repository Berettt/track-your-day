# Generated by Django 4.0.5 on 2022-09-18 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('track_day', '0002_taskday_opis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('tasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track_day.taskday')),
            ],
        ),
    ]
