# Generated by Django 2.0 on 2021-10-16 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readersnook', '0009_auto_20211011_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('author', models.TextField(max_length=50)),
                ('genre', models.TextField(max_length=30)),
                ('description', models.TextField(max_length=200, null=True)),
                ('day', models.TextField(max_length=30)),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('author', models.TextField(max_length=50)),
                ('genre', models.TextField(max_length=30)),
                ('description', models.TextField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'misc',
            },
        ),
        migrations.CreateModel(
            name='w_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('author', models.TextField(max_length=50)),
                ('genre', models.TextField(max_length=30)),
                ('description', models.TextField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'w_item',
            },
        ),
    ]
