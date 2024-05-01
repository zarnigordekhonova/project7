# Generated by Django 5.0.4 on 2024-05-01 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('based_on_book', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_awards', models.IntegerField()),
                ('rate_percentage_on_ImDB', models.IntegerField()),
            ],
        ),
    ]
