# Generated by Django 3.2.18 on 2023-05-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocietyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('societyName', models.CharField(max_length=122)),
                ('regno', models.CharField(max_length=122)),
                ('address', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]