# Generated by Django 3.0.4 on 2020-04-02 09:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='news_photo/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='news_photo/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 9, 32, 37, 541156, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(blank=True, max_length=250, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.NewsModel')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
