# Generated by Django 4.1.7 on 2023-06-14 14:52

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('idutilisateur', models.AutoField(db_column='idutilisateur', primary_key=True, serialize=False)),
                ('cin', models.CharField(db_column='CIN', max_length=20)),
                ('n_som', models.CharField(db_column='N_SOM', max_length=30)),
                ('nomfr', models.CharField(db_column='NOMFR', max_length=30)),
                ('nomar', models.CharField(db_column='NOMAR', max_length=30)),
                ('prenomfr', models.CharField(db_column='PRENOMFR', max_length=30)),
                ('prenomar', models.CharField(db_column='PRENOMAR', max_length=30)),
                ('telephone', models.CharField(db_column='TELEPHONE', max_length=20)),
                ('password', models.CharField(db_column='PASSWORD', max_length=250)),
                ('email', models.CharField(db_column='EMAIL', max_length=254)),
                ('profilepic', models.ImageField(blank=True, db_column='picurl', null=True, upload_to='profiles-pics/')),
                ('username', models.CharField(db_column='USERNAME', max_length=150, unique=True)),
                ('is_superuser', models.BooleanField(db_column='is_superuser', default=False)),
                ('is_active', models.BooleanField(db_column='is_active', default=True)),
                ('is_staff', models.BooleanField(db_column='is_staff', default=False)),
                ('isadmine', models.BooleanField(db_column='isadmine', default=False)),
            ],
            options={
                'db_table': 'utilisateur',
                'managed': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('idadre', models.IntegerField(db_column='IDADRE', primary_key=True, serialize=False)),
                ('nummaison', models.CharField(blank=True, db_column='NUMMAISON', max_length=20, null=True)),
                ('rue', models.CharField(blank=True, db_column='RUE', max_length=50, null=True)),
                ('commune', models.CharField(blank=True, db_column='COMMUNE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'adresse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('idannonce', models.AutoField(db_column='IDANNONCE', primary_key=True, serialize=False)),
                ('dateannonce', models.DateField(db_column='DATEANNONCE')),
                ('titreannonce', models.CharField(db_column='TITREANNONCE', max_length=150)),
                ('contenu', models.TextField(db_column='CONTENU')),
            ],
            options={
                'db_table': 'annonce',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bac',
            fields=[
                ('codebac', models.CharField(db_column='CODEBAC', max_length=30, primary_key=True, serialize=False)),
                ('serie', models.CharField(blank=True, db_column='SERIE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'bac',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('iddemande', models.AutoField(db_column='IDdemande', primary_key=True, serialize=False)),
                ('date_deman', models.DateField(db_column='Date_deman')),
                ('etatdeman', models.CharField(db_column='EtatDeman', max_length=30)),
                ('datetraitement', models.DateField(db_column='DateTraitement')),
            ],
            options={
                'db_table': 'demande',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('iddept', models.CharField(db_column='IDDEPT', max_length=30, primary_key=True, serialize=False)),
                ('intituledept', models.CharField(db_column='INTITULEDEPT', max_length=50)),
            ],
            options={
                'db_table': 'departement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailEnum',
            fields=[
                ('id_detail', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('libelle_fr', models.CharField(blank=True, db_column='LIBELLE_FR', max_length=50, null=True)),
                ('libelle_ar', models.CharField(blank=True, db_column='LIBELLE_AR', max_length=50, null=True)),
            ],
            options={
                'db_table': 'detail_enum',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diplome',
            fields=[
                ('codediplome', models.IntegerField(db_column='CODEDIPLOME', primary_key=True, serialize=False)),
                ('intitulediplomefr', models.CharField(blank=True, db_column='INTITULEDIPLOMEFR', max_length=50, null=True)),
                ('intitulediplomear', models.CharField(blank=True, db_column='INTITULEDIPLOMEAR', max_length=50, null=True)),
                ('niveau', models.CharField(blank=True, db_column='Niveau', max_length=20, null=True)),
            ],
            options={
                'db_table': 'diplome',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enum',
            fields=[
                ('id2', models.IntegerField(db_column='ID2', primary_key=True, serialize=False)),
                ('nom_enum', models.CharField(blank=True, db_column='NOM_ENUM', max_length=50, null=True)),
            ],
            options={
                'db_table': 'enum',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Etablissementbac',
            fields=[
                ('idetablissmentbac', models.IntegerField(db_column='IDETABLISSMENTBAC', primary_key=True, serialize=False)),
                ('nometablissement', models.CharField(blank=True, db_column='NOMETABLISSEMENT', max_length=50, null=True)),
            ],
            options={
                'db_table': 'etablissementbac',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Etablissementbp',
            fields=[
                ('idetablissementbp', models.CharField(db_column='IDETABLISSEMENTBP', max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, db_column='TYPE', max_length=30, null=True)),
                ('intituleetablissementbp', models.CharField(blank=True, db_column='INTITULEETABLISSEMENTBP', max_length=30, null=True)),
            ],
            options={
                'db_table': 'etablissementbp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('apogee', models.IntegerField(db_column='APOGEE', primary_key=True, serialize=False)),
                ('nomar', models.CharField(blank=True, db_column='NOMAR', max_length=30, null=True)),
                ('nomfr', models.CharField(blank=True, db_column='NOMFR', max_length=30, null=True)),
                ('prenomar', models.CharField(blank=True, db_column='PRENOMAR', max_length=30, null=True)),
                ('prenomfr', models.CharField(blank=True, db_column='PRENOMFR', max_length=30, null=True)),
                ('ddn', models.CharField(blank=True, db_column='DDN', max_length=30, null=True)),
                ('villenaissfr', models.CharField(blank=True, db_column='VILLENAISSFR', max_length=50, null=True)),
                ('villenaissar', models.CharField(blank=True, db_column='VILLENAISSAR', max_length=50, null=True)),
                ('adresse_fr', models.CharField(db_column='Adresse_FR', max_length=50)),
                ('adresse_ar', models.CharField(db_column='Adresse_AR', max_length=50)),
                ('adresse_ur_fr', models.CharField(db_column='Adresse_UR_FR', max_length=50)),
                ('adresse_ur_ar', models.CharField(db_column='Adresse_UR_AR', max_length=50)),
                ('rib', models.CharField(blank=True, db_column='RIB', max_length=40, null=True)),
                ('boursier', models.IntegerField(blank=True, db_column='BOURSIER', null=True)),
                ('telephone', models.CharField(blank=True, db_column='TELEPHONE', max_length=20, null=True)),
                ('email', models.CharField(db_column='EMAIL', max_length=30, unique=True)),
                ('situationfam', models.CharField(blank=True, db_column='SITUATIONFAM', max_length=20, null=True)),
                ('pays', models.CharField(blank=True, db_column='PAYS', max_length=20, null=True)),
                ('sexe', models.CharField(blank=True, db_column='SEXE', max_length=10, null=True)),
                ('telurgence', models.CharField(blank=True, db_column='TELURGENCE', max_length=20, null=True)),
                ('photo', models.CharField(blank=True, db_column='PHOTO', max_length=100, null=True)),
                ('nomperear', models.CharField(blank=True, db_column='NOMPEREAR', max_length=30, null=True)),
                ('cin', models.CharField(blank=True, db_column='CIN', max_length=20, null=True)),
                ('massarcne', models.CharField(blank=True, db_column='MASSARCNE', max_length=20, null=True)),
                ('motdepasse', models.CharField(blank=True, db_column='MOTDEPASSE', max_length=20, null=True)),
            ],
            options={
                'db_table': 'etudiant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('n_examen', models.IntegerField(db_column='N_EXAMEN')),
                ('h_debut', models.DateTimeField(db_column='h_Debut')),
                ('h_fin', models.DateTimeField(db_column='h_Fin')),
                ('note', models.DecimalField(blank=True, db_column='NOTE', decimal_places=2, max_digits=4, null=True)),
                ('resultat', models.IntegerField(blank=True, db_column='RESULTAT', null=True)),
                ('session', models.CharField(blank=True, db_column='SESSION', max_length=150, null=True)),
            ],
            options={
                'db_table': 'examen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id_filiere', models.IntegerField(db_column='ID_FILIERE', primary_key=True, serialize=False)),
                ('intulite_ar', models.CharField(blank=True, db_column='INTULITE_AR', max_length=50, null=True)),
                ('intulite_fr', models.CharField(blank=True, db_column='INTULITE_FR', max_length=50, null=True)),
            ],
            options={
                'db_table': 'filiere',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('idgrade', models.AutoField(db_column='IDGRADE', primary_key=True, serialize=False)),
                ('intitulegrade', models.CharField(blank=True, db_column='INTITULEGRADE', max_length=20, null=True)),
            ],
            options={
                'db_table': 'grade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Handicap',
            fields=[
                ('numerohandicap', models.CharField(db_column='NUMEROHANDICAP', max_length=30, primary_key=True, serialize=False)),
                ('typehandicap', models.CharField(blank=True, db_column='TYPEHANDICAP', max_length=30, null=True)),
            ],
            options={
                'db_table': 'handicap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Langue',
            fields=[
                ('id_langue', models.IntegerField(db_column='ID_LANGUE', primary_key=True, serialize=False)),
                ('intulite', models.CharField(blank=True, db_column='INTULITE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'langue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id_local', models.IntegerField(db_column='ID_LOCAL', primary_key=True, serialize=False)),
                ('num_local', models.IntegerField(blank=True, db_column='NUM_LOCAL', null=True)),
                ('capacite', models.IntegerField(blank=True, db_column='CAPACITE', null=True)),
                ('type', models.CharField(blank=True, db_column='TYPE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id_modmat', models.CharField(db_column='ID_MODMAT', max_length=30, primary_key=True, serialize=False)),
                ('intulite_ar', models.CharField(blank=True, db_column='INTULITE_AR', max_length=50, null=True)),
                ('intulite_fr', models.CharField(blank=True, db_column='INTULITE_FR', max_length=50, null=True)),
                ('volume_horaire', models.IntegerField(blank=True, db_column='VOLUME_HORAIRE', null=True)),
                ('nbr_matiere', models.IntegerField(blank=True, db_column='NBR_MATIERE', null=True)),
                ('type', models.CharField(blank=True, db_column='TYPE', max_length=30, null=True)),
                ('id_modupere', models.CharField(blank=True, db_column='ID_MODUPERE', max_length=30, null=True)),
                ('id_modprerequi', models.CharField(db_column='ID_MODPREREQUI', max_length=30)),
            ],
            options={
                'db_table': 'module',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id_reclamation', models.AutoField(db_column='ID_RECLAMATION', primary_key=True, serialize=False)),
                ('date_reclamation', models.DateField(blank=True, db_column='DATE_RECLAMATION', null=True)),
                ('commentaire', models.TextField(blank=True, db_column='COMMENTAIRE', null=True)),
            ],
            options={
                'db_table': 'reclamation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id_semestre', models.IntegerField(db_column='ID_SEMESTRE', primary_key=True, serialize=False)),
                ('intulite_semestre', models.CharField(blank=True, db_column='INTULITE_SEMESTRE', max_length=20, null=True)),
            ],
            options={
                'db_table': 'semestre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('idspec', models.AutoField(db_column='IDSPEC', primary_key=True, serialize=False)),
                ('intitulespec', models.CharField(db_column='INTITULESPEC', max_length=30)),
            ],
            options={
                'db_table': 'specialite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypeEnseigner',
            fields=[
                ('id_types', models.IntegerField(db_column='ID_TYPES', primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, db_column='TYPE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'type_enseigner',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('codepostal', models.IntegerField(db_column='CODEPOSTAL', primary_key=True, serialize=False)),
                ('intituleville', models.CharField(blank=True, db_column='INTITULEVILLE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'ville',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Adresseetud',
            fields=[
                ('idadre', models.OneToOneField(db_column='IDADRE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.adresse')),
            ],
            options={
                'db_table': 'adresseetud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id_local', models.OneToOneField(db_column='ID_LOCAL', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.local')),
                ('n_examen', models.IntegerField(db_column='N_EXAMEN')),
                ('h_debut', models.DateTimeField(db_column='h_Debut')),
                ('h_fin', models.DateTimeField(db_column='h_Fin')),
                ('note', models.DecimalField(blank=True, db_column='NOTE', decimal_places=2, max_digits=4, null=True)),
                ('resultat', models.IntegerField(blank=True, db_column='RESULTAT', null=True)),
                ('session', models.CharField(blank=True, db_column='SESSION', max_length=150, null=True)),
            ],
            options={
                'db_table': 'examen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gradeprof',
            fields=[
                ('idgrade', models.OneToOneField(db_column='IDGRADE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.grade')),
                ('date', models.DateField(db_column='DATE')),
            ],
            options={
                'db_table': 'gradeprof',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Handietud',
            fields=[
                ('numerohandicap', models.OneToOneField(db_column='NUMEROHANDICAP', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.handicap')),
            ],
            options={
                'db_table': 'handietud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inscritbac',
            fields=[
                ('apogee', models.OneToOneField(db_column='APOGEE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.etudiant')),
                ('annee', models.IntegerField(blank=True, db_column='ANNEE', null=True)),
                ('note', models.DecimalField(blank=True, db_column='NOTE', decimal_places=2, max_digits=4, null=True)),
                ('mention', models.CharField(blank=True, db_column='MENTION', max_length=20, null=True)),
            ],
            options={
                'db_table': 'inscritbac',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inscritdip',
            fields=[
                ('codediplome', models.OneToOneField(db_column='CODEDIPLOME', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.diplome')),
                ('annee', models.IntegerField(blank=True, db_column='ANNEE', null=True)),
                ('note', models.DecimalField(blank=True, db_column='NOTE', decimal_places=2, max_digits=4, null=True)),
                ('mention', models.CharField(blank=True, db_column='MENTION', max_length=20, null=True)),
            ],
            options={
                'db_table': 'inscritdip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InscritModul',
            fields=[
                ('id_modmat', models.OneToOneField(db_column='ID_MODMAT', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.module')),
                ('annee', models.IntegerField(blank=True, db_column='ANNEE', null=True)),
                ('note_examen', models.IntegerField(blank=True, db_column='NOTE_EXAMEN', null=True)),
                ('resultat', models.IntegerField(blank=True, db_column='RESULTAT', null=True)),
                ('observaion', models.CharField(blank=True, db_column='OBSERVAION', max_length=150, null=True)),
            ],
            options={
                'db_table': 'inscrit_modul',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Intervenir',
            fields=[
                ('idutilisateur', models.OneToOneField(db_column='idutilisateur', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('annee', models.IntegerField(blank=True, db_column='ANNEE', null=True)),
                ('type', models.CharField(blank=True, db_column='TYPE', max_length=30, null=True)),
            ],
            options={
                'db_table': 'intervenir',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModFilSem',
            fields=[
                ('id_modmat', models.OneToOneField(db_column='ID_MODMAT', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.module')),
            ],
            options={
                'db_table': 'mod_fil_sem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModuleLangue',
            fields=[
                ('id_modmat', models.OneToOneField(db_column='ID_MODMAT', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.module')),
            ],
            options={
                'db_table': 'module_langue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModuleTypeEns',
            fields=[
                ('id_modmat', models.OneToOneField(db_column='ID_MODMAT', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.module')),
            ],
            options={
                'db_table': 'module_type_ens',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParcoursTypeDesciplin',
            fields=[
                ('id_modmat', models.OneToOneField(db_column='ID_MODMAT', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.module')),
            ],
            options={
                'db_table': 'parcours_type_desciplin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProffessTypreside',
            fields=[
                ('apogee', models.OneToOneField(db_column='APOGEE', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.etudiant')),
            ],
            options={
                'db_table': 'proffess_typreside',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Universofpp',
            fields=[
                ('idetablissementbp', models.OneToOneField(db_column='IDETABLISSEMENTBP', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.etablissementbp')),
            ],
            options={
                'db_table': 'universofpp',
                'managed': False,
            },
        ),
    ]
