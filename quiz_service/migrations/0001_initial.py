# Generated by Django 3.0.8 on 2020-11-22 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_number', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('quiz_contents', models.TextField()),
                ('example1', models.TextField()),
                ('example2', models.TextField()),
                ('example3', models.TextField()),
                ('example4', models.TextField()),
                ('correct', models.IntegerField()),
                ('subject', models.TextField()),
                ('detail_subject', models.TextField()),
                ('bookmark_count', models.IntegerField()),
                ('correct_count', models.IntegerField()),
                ('wrong_count', models.IntegerField()),
                ('reveal_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
