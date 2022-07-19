# Generated by Django 4.0.6 on 2022-07-18 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]