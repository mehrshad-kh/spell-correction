# Generated by Django 5.1.4 on 2025-01-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='G25Dataset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'G2_5_dataset',
            },
        ),
    ]