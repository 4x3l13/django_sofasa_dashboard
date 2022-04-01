# Generated by Django 4.0.2 on 2022-03-02 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlotaEntrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17)),
                ('placa', models.CharField(max_length=6)),
                ('fecha_venta', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('cliente_juridico', models.CharField(max_length=80)),
                ('identificacion_juridico', models.CharField(max_length=15)),
                ('contacto_juridico', models.CharField(max_length=50)),
                ('identificacion_contacto', models.CharField(max_length=12)),
                ('ciudad_contacto', models.SmallIntegerField()),
                ('direccion_contacto', models.CharField(max_length=50)),
                ('telefono_contacto', models.CharField(max_length=20)),
                ('celular_contacto', models.CharField(max_length=30)),
                ('email_contacto', models.EmailField(max_length=50)),
                ('cargo_contacto', models.CharField(max_length=50)),
                ('estado', models.BooleanField()),
            ],
        ),
    ]