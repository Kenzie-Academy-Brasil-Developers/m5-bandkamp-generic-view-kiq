# Generated by Django 4.0.7 on 2022-12-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
