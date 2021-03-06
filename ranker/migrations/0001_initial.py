# Generated by Django 2.0.8 on 2018-09-02 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_handle',
            fields=[
                ('handle_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_location', models.CharField(max_length=50)),
                ('joining_date', models.CharField(max_length=50)),
                ('world_rank', models.IntegerField()),
                ('points', models.FloatField()),
                ('institution', models.TextField(max_length=50)),
                ('problems_solved', models.IntegerField()),
                ('total_submissions', models.IntegerField()),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
