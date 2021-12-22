# Generated by Django 3.1.3 on 2020-11-30 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('url', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='Published at')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('text', models.TextField()),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=256)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]