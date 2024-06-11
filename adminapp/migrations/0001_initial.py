# Generated by Django 5.0.4 on 2024-05-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=50)),
                ('mfgdate', models.CharField(max_length=30)),
                ('expdate', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('productpic', models.FileField(upload_to='')),
            ],
        ),
    ]
