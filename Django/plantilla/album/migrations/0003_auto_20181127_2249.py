# Generated by Django 2.1.2 on 2018-11-28 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_photo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
