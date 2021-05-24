# Generated by Django 3.0.11 on 2021-04-20 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Events Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('featured_image', models.ImageField(blank=True, default='img_default.jpg', null=True, upload_to='static/images/events')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('venue', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('tags', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_edited', models.DateField(auto_now_add=True)),
                ('featured', models.BooleanField()),
                ('block', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.Category')),
                ('student', models.ManyToManyField(to='account.StudentUser')),
                ('teacher', models.ManyToManyField(to='account.TeacherUser')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='img_default.jpg', null=True, upload_to='static/images/gallery')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
        ),
    ]
