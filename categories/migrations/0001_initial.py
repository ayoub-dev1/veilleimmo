# Generated by Django 2.2.3 on 2020-01-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(max_length=128)),
                ('update', models.DateTimeField(auto_now=True)),
                ('date_enregistrement', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
