# Generated by Django 4.2.1 on 2023-05-11 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_movie_studios_alter_movie_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie_producer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]