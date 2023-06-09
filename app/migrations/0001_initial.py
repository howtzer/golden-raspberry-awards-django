# Generated by Django 4.2.1 on 2023-05-10 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('studios', models.CharField(max_length=255)),
                ('winner', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('producer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_producer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.movie')),
                ('producer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producer')),
            ],
        ),
    ]
