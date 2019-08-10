# Generated by Django 2.2.4 on 2019-08-10 15:32

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgurConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_limit', models.IntegerField(default=1000, validators=[django.core.validators.MinValueValidator(0)])),
                ('allow_albums', models.BooleanField(default=True)),
                ('good_tags', models.TextField(blank=True, help_text='List of good tags. Should be separated with comma.')),
                ('bad_tags', models.TextField(blank=True, help_text='List of bad tags. Should be separated with comma.')),
                ('exclude_mode', models.BooleanField(default=True, help_text='If true then posts with bad tags will be filtered out. Otherwise only posts from with good tags will pass the filter.')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgur_id', models.CharField(max_length=200)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('score', models.IntegerField()),
                ('is_album', models.BooleanField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=list, size=None)),
                ('media_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list)),
                ('images_count', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imgur.ImgurConfig')),
            ],
        ),
    ]
