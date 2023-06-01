# Generated by Django 3.2.14 on 2023-05-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompositeKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_examen', models.IntegerField(db_column='N_EXAMEN')),
                ('h_debut', models.DateTimeField(db_column='h_Debut')),
            ],
            options={
                'db_table': 'examen',
                'managed': False,
            },
        ),
    ]
