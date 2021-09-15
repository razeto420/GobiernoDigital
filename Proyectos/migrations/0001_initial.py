# Generated by Django 3.2.7 on 2021-09-15 00:59

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
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('presupuesto', models.FloatField()),
                ('responsable', models.CharField(max_length=50)),
                ('monto_cancelado', models.FloatField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final_esperado', models.DateField()),
                ('fecha_culminado', models.DateField(blank=True, null=True)),
                ('adenda', models.CharField(blank=True, max_length=100, null=True)),
                ('monto_adenda', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyectos.provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyectos.proyecto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
