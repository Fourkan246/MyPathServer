# Generated by Django 4.0.3 on 2023-04-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('st', models.CharField(max_length=25)),
                ('et', models.CharField(max_length=20)),
                ('sbt', models.IntegerField()),
            ],
        ),
    ]