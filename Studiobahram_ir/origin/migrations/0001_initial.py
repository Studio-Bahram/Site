# Generated by Django 3.0.5 on 2020-05-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instruction TITLE', models.CharField(max_length=400)),
                ('slug', models.SlugField(unique=True)),
                ('pub_date', models.DateField()),
                ('instruction_text', models.TextField(help_text='Writeing text Instruction ...')),
                ('YOUTUBE URL', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('pub_date', models.DateField()),
                ('picture', models.ImageField(default='db_files/posts/pics/%Y/%m/%d/img.jpg', upload_to='db_files/posts/pics/%Y/%m/%d/')),
                ('file_post', models.FileField(default='db_files/posts/files/%Y/%m/%d/file', upload_to='db_files/posts/files/%Y/%m/%d/')),
                ('about_post', models.TextField(help_text='Writeing about post ...')),
                ('github_url', models.URLField(default='https://github.com/', max_length=300)),
            ],
        ),
    ]
