# Generated by Django 3.2.6 on 2021-08-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('insta', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='pics')),
                ('github', models.CharField(max_length=200)),
            ],
        ),
    ]