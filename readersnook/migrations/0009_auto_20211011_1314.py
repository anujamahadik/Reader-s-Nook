# Generated by Django 2.0 on 2021-10-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readersnook', '0008_communication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('author', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('pdf', models.FileField(upload_to='pdf')),
                ('recommended_books', models.BooleanField(default=False)),
                ('fiction_books', models.BooleanField(default=False)),
                ('business_books', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BookSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Categories')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', to='readersnook.Category'),
        ),
    ]