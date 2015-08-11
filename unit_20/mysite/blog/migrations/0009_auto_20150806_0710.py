# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Published'), (2, b'Hidden')])),
                ('title', models.CharField(max_length=32)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('featured_image', models.ImageField(max_length=1024, null=True, upload_to=blog.models.get_blog_file_name, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Published'), (2, b'Hidden')])),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(max_length=1024, null=True, upload_to=blog.models.get_blog_file_name, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Published'), (2, b'Hidden')])),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='slide',
            name='related_slider',
            field=models.ForeignKey(to='blog.Slider'),
        ),
        migrations.AddField(
            model_name='page',
            name='related_slider',
            field=models.ForeignKey(blank=True, to='blog.Slider', null=True),
        ),
    ]
