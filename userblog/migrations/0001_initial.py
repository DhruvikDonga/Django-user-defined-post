# Generated by Django 3.0.1 on 2020-01-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogname', models.CharField(max_length=100)),
                ('blogauth', models.CharField(max_length=100)),
                ('blogdes', models.CharField(max_length=400)),
            ],
        ),
    ]
