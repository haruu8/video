# Generated by Django 3.1 on 2020-09-02 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('discription', models.CharField(max_length=355, null=True)),
                ('movie', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'movie',
            },
        ),
    ]
