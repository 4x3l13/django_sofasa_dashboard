# Generated by Django 4.0.2 on 2022-03-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('graph_encuesta', 'Can graph encuesta'), ('download_encuesta', 'Can download encuesta'), ('search_encuesta', 'Can search encuesta')),
            },
        ),
    ]
