# Generated by Django 5.0.4 on 2024-04-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(upload_to='profile_picture/')),
            ],
        ),
    ]
