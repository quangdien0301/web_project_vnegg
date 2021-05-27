# Generated by Django 3.1.7 on 2021-03-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('educator', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=1000)),
                ('excerpt', models.TextField(default='', max_length=300)),
                ('num_lessons', models.PositiveSmallIntegerField(default=0)),
                ('picture', models.ImageField(upload_to='course_picture')),
            ],
        ),
    ]
