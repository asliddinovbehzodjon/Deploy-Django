# Generated by Django 4.1.3 on 2022-11-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter title', max_length=200, verbose_name='Title')),
                ('body', models.TextField(help_text='Enter post description', verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Post ',
                'verbose_name_plural': 'Posts ',
            },
        ),
    ]