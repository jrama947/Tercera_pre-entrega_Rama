# Generated by Django 4.2 on 2023-10-05 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('difficulty', models.CharField(max_length=30)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Alojamientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=20)),
                ('stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Atracciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Destinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('popularity', models.IntegerField()),
            ],
        ),
    ]
