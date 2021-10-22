# Generated by Django 3.2.5 on 2021-09-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('Type', models.CharField(max_length=100)),
                ('Depth', models.FloatField()),
                ('Magnitude', models.FloatField()),
                ('Magnitude_type', models.CharField(max_length=100)),
                ('ID', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Quake',
            },
        ),
    ]
