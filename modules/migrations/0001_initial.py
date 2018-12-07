# Generated by Django 2.0.6 on 2018-12-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('duration', models.DateTimeField()),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
