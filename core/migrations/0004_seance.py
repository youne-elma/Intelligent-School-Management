# Generated by Django 4.1.7 on 2023-06-22 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_reports'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('idseance', models.IntegerField(db_column='IDSEANCE', primary_key=True, serialize=False)),
                ('titreseance', models.CharField(db_column='TITRESEANCE', max_length=150)),
                ('datedebut', models.DateTimeField(db_column='DATEDEBUT', null=True)),
                ('datefin', models.DateTimeField(db_column='DATEFIN', null=True)),
                ('details', models.CharField(db_column='DETAILS', max_length=150)),
                ('section', models.CharField(db_column='SECTION', max_length=30)),
                ('groupe', models.CharField(db_column='GROUPE', max_length=30)),
                ('filiere', models.CharField(db_column='FILIERE', max_length=30)),
                ('salle', models.CharField(db_column='SALLE', max_length=30)),
            ],
            options={
                'db_table': 'seance',
                'managed': False,
            },
        ),
    ]
