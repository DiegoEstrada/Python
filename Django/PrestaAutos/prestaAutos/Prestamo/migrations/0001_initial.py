# Generated by Django 2.1.2 on 2018-12-06 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Automovil', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(auto_now=True)),
                ('fecha_fin', models.DateField()),
                ('observciones', models.TextField(blank=True)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Automovil.Automovil')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPrestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('dias', models.IntegerField()),
            ],
        ),
    ]
