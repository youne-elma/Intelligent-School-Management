# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class utilisateur(AbstractUser):
    idutilisateur = models.AutoField(db_column='idutilisateur', primary_key=True)  # Field name made lowercase.
    idspec = models.ForeignKey('Specialite', models.DO_NOTHING, db_column='IDSPEC')  # Field name made lowercase.
    iddept = models.ForeignKey('Departement', models.DO_NOTHING, db_column='IDDEPT')  # Field name made lowercase.
    cin = models.CharField(db_column='CIN', max_length=20)  # Field name made lowercase.
    n_som = models.CharField(db_column='N_SOM', max_length=30)  # Field name made lowercase.
    nomfr = models.CharField(db_column='NOMFR', max_length=30)  # Field name made lowercase.""
    nomar = models.CharField(db_column='NOMAR', max_length=30)  # Field name made lowercase.
    prenomfr = models.CharField(db_column='PRENOMFR', max_length=30)  # Field name made lowercase.
    prenomar = models.CharField(db_column='PRENOMAR', max_length=30)  # Field name made lowercase.
    telephone = models.CharField(db_column='TELEPHONE', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD',max_length=250)
    email = models.CharField(db_column='EMAIL',max_length=254)
    profilepic  = models.ImageField(db_column='picurl', upload_to='profiles-pics/', null=True, blank=True)
    username = models.CharField(db_column='USERNAME',unique=True, max_length=150)
    is_superuser = models.BooleanField(db_column='is_superuser',default=False)
    is_active = models.BooleanField(db_column='is_active',default=True)
    is_staff = models.BooleanField(db_column='is_staff',default=False)
    isadmine = models.BooleanField(db_column='isadmine',default=False)
    profilepic  = models.ImageField(db_column='picurl', upload_to='profiles-pics/', null=True, blank=True)
    last_name = None
    first_name = None
    last_login = None
    date_joined = None

    groups = models.ManyToManyField(Group, related_name='core_utilisateurs')
    user_permissions = models.ManyToManyField(
        Permission, related_name='core_utilisateurs'
    )

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'utilisateur'

class Adresse(models.Model):
    idadre = models.IntegerField(db_column='IDADRE', primary_key=True)  # Field name made lowercase.
    codepostal = models.ForeignKey('Ville', models.DO_NOTHING, db_column='CODEPOSTAL')  # Field name made lowercase.
    nummaison = models.CharField(db_column='NUMMAISON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rue = models.CharField(db_column='RUE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    commune = models.CharField(db_column='COMMUNE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adresse'


class Adresseetud(models.Model):
    idadre = models.OneToOneField(Adresse, models.DO_NOTHING, db_column='IDADRE', primary_key=True)  # Field name made lowercase. The composite primary key (IDADRE, APOGEE) found, that is not supported. The first column is selected.
    apogee = models.ForeignKey('Etudiant', models.DO_NOTHING, db_column='APOGEE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adresseetud'
        unique_together = (('idadre', 'apogee'),)


class Annonce(models.Model):
    idannonce = models.AutoField(db_column='IDANNONCE', primary_key=True)  # Field name made lowercase.
    id_semestre = models.ForeignKey('Semestre', models.DO_NOTHING, db_column='ID_SEMESTRE')  # Field name made lowercase.
    apogee = models.ForeignKey('Etudiant', models.DO_NOTHING, db_column='APOGEE')  # Field name made lowercase.
    id_modmat = models.ForeignKey('Module', models.DO_NOTHING, db_column='ID_MODMAT')  # Field name made lowercase.
    idutilisateur = models.ForeignKey('utilisateur', models.DO_NOTHING, db_column='IDutilisateur')  # Field name made lowercase.
    dateannonce = models.DateField(db_column='DATEANNONCE')  # Field name made lowercase.
    titreannonce = models.CharField(db_column='TITREANNONCE', max_length=150)  # Field name made lowercase.
    contenu = models.TextField(db_column='CONTENU')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'annonce'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bac(models.Model):
    codebac = models.CharField(db_column='CODEBAC', primary_key=True, max_length=30)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bac'


class Demande(models.Model):
    iddemande = models.AutoField(db_column='IDdemande', primary_key=True)  # Field name made lowercase.
    date_deman = models.DateField(db_column='Date_deman')  # Field name made lowercase.
    etatdeman = models.CharField(db_column='EtatDeman', max_length=30)  # Field name made lowercase.
    datetraitement = models.DateField(db_column='DateTraitement')  # Field name made lowercase.
    idetaildemande = models.ForeignKey('DetailEnum', models.DO_NOTHING, db_column='IDetaildemande')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'demande'


class Departement(models.Model):
    iddept = models.CharField(db_column='IDDEPT', primary_key=True, max_length=30)  # Field name made lowercase.
    intituledept = models.CharField(db_column='INTITULEDEPT', max_length=50)  # Field name made lowercase.
    id_profchef = models.ForeignKey('utilisateur', models.DO_NOTHING, db_column='ID_PROFCHEF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departement'


class DetailEnum(models.Model):
    id_detail = models.CharField(primary_key=True, max_length=50)
    id2 = models.ForeignKey('Enum', models.DO_NOTHING, db_column='ID2')  # Field name made lowercase.
    libelle_fr = models.CharField(db_column='LIBELLE_FR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    libelle_ar = models.CharField(db_column='LIBELLE_AR', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detail_enum'


class Diplome(models.Model):
    codediplome = models.IntegerField(db_column='CODEDIPLOME', primary_key=True)  # Field name made lowercase.
    intitulediplomefr = models.CharField(db_column='INTITULEDIPLOMEFR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intitulediplomear = models.CharField(db_column='INTITULEDIPLOMEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_detail = models.ForeignKey(DetailEnum, models.DO_NOTHING, db_column='ID_DETAIL', blank=True, null=True)  # Field name made lowercase.
    niveau = models.CharField(db_column='Niveau', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diplome'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enum(models.Model):
    id2 = models.IntegerField(db_column='ID2', primary_key=True)  # Field name made lowercase.
    nom_enum = models.CharField(db_column='NOM_ENUM', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enum'


class Etablissementbac(models.Model):
    idetablissmentbac = models.IntegerField(db_column='IDETABLISSMENTBAC', primary_key=True)  # Field name made lowercase.
    nometablissement = models.CharField(db_column='NOMETABLISSEMENT', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etablissementbac'


class Etablissementbp(models.Model):
    idetablissementbp = models.CharField(db_column='IDETABLISSEMENTBP', primary_key=True, max_length=20)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    intituleetablissementbp = models.CharField(db_column='INTITULEETABLISSEMENTBP', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etablissementbp'


class Etudiant(models.Model):
    apogee = models.IntegerField(db_column='APOGEE', primary_key=True)  # Field name made lowercase.
    nomar = models.CharField(db_column='NOMAR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomfr = models.CharField(db_column='NOMFR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prenomar = models.CharField(db_column='PRENOMAR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prenomfr = models.CharField(db_column='PRENOMFR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ddn = models.CharField(db_column='DDN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    villenaissfr = models.CharField(db_column='VILLENAISSFR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    villenaissar = models.CharField(db_column='VILLENAISSAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adresse_fr = models.CharField(db_column='Adresse_FR', max_length=50)  # Field name made lowercase.
    adresse_ar = models.CharField(db_column='Adresse_AR', max_length=50)  # Field name made lowercase.
    adresse_ur_fr = models.CharField(db_column='Adresse_UR_FR', max_length=50)  # Field name made lowercase.
    adresse_ur_ar = models.CharField(db_column='Adresse_UR_AR', max_length=50)  # Field name made lowercase.
    rib = models.CharField(db_column='RIB', max_length=40, blank=True, null=True)  # Field name made lowercase.
    boursier = models.IntegerField(db_column='BOURSIER', blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TELEPHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=30)  # Field name made lowercase.
    situationfam = models.CharField(db_column='SITUATIONFAM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pays = models.CharField(db_column='PAYS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='SEXE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    telurgence = models.CharField(db_column='TELURGENCE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    photo = models.CharField(db_column='PHOTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomperear = models.CharField(db_column='NOMPEREAR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cin = models.CharField(db_column='CIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    massarcne = models.CharField(db_column='MASSARCNE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    motdepasse = models.CharField(db_column='MOTDEPASSE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etudiant'


class Examen(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    id_local = models.ForeignKey('Local', models.DO_NOTHING, db_column='ID_LOCAL')  # Field name made lowercase. The composite primary key (ID_LOCAL, APOGEE, ID_MODMAT, N_EXAMEN, h_Debut) found, that is not supported. The first column is selected.
    apogee = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='APOGEE')  # Field name made lowercase.
    id_modmat = models.ForeignKey('Module', models.DO_NOTHING, db_column='ID_MODMAT')  # Field name made lowercase.
    n_examen = models.IntegerField(db_column='N_EXAMEN')  # Field name made lowercase.
    h_debut = models.DateTimeField(db_column='h_Debut')  # Field name made lowercase.
    h_fin = models.DateTimeField(db_column='h_Fin')  # Field name made lowercase.
    note = models.DecimalField(db_column='NOTE', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    resultat = models.IntegerField(db_column='RESULTAT', blank=True, null=True)  # Field name made lowercase.
    session = models.CharField(db_column='SESSION', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'examen'
        unique_together = (('id_local', 'apogee', 'id_modmat', 'n_examen', 'h_debut'))

class Chat(models.Model):
    
    user_id = models.ForeignKey(utilisateur, models.DO_NOTHING, db_column='user_id', related_name='sent_chat')  # Field name made lowercase.
    message = models.TextField(db_column='message')  # Field name made lowercase.
    date = models.DateTimeField(db_column='date')  # Field name made lowercase.
    destination = models.ForeignKey(utilisateur, models.DO_NOTHING, db_column='destination' ,related_name='received_chat')# Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chat'
        unique_together = (('user_id', 'date', 'destination'),)
        
class Reports(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    report_message = models.TextField(db_column='report_message')  # Field name made lowercase. 
    date = models.DateTimeField(db_column='date')  # Field name made lowercase.
    log = models.TextField(db_column='log')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Reports'
class Filiere(models.Model):
    id_filiere = models.IntegerField(db_column='ID_FILIERE', primary_key=True)  # Field name made lowercase.
    iddept = models.ForeignKey(Departement, models.DO_NOTHING, db_column='IDDEPT')  # Field name made lowercase.
    intulite_ar = models.CharField(db_column='INTULITE_AR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intulite_fr = models.CharField(db_column='INTULITE_FR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_profcord = models.ForeignKey('utilisateur', models.DO_NOTHING, db_column='ID_PROFCORD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'filiere'


class Grade(models.Model):
    idgrade = models.AutoField(db_column='IDGRADE', primary_key=True)  # Field name made lowercase.
    intitulegrade = models.CharField(db_column='INTITULEGRADE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grade'


class Gradeprof(models.Model):
    idgrade = models.OneToOneField(Grade, models.DO_NOTHING, db_column='IDGRADE', primary_key=True)  # Field name made lowercase. The composite primary key (IDGRADE, idutilisateur) found, that is not supported. The first column is selected.
    idutilisateur = models.ForeignKey('utilisateur', models.DO_NOTHING, db_column='idutilisateur')  # Field name made lowercase.
    date = models.DateField(db_column='DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gradeprof'
        unique_together = (('idgrade', 'idutilisateur'),)


class Handicap(models.Model):
    numerohandicap = models.CharField(db_column='NUMEROHANDICAP', primary_key=True, max_length=30)  # Field name made lowercase.
    typehandicap = models.CharField(db_column='TYPEHANDICAP', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'handicap'


class Handietud(models.Model):
    numerohandicap = models.OneToOneField(Handicap, models.DO_NOTHING, db_column='NUMEROHANDICAP', primary_key=True)  # Field name made lowercase. The composite primary key (NUMEROHANDICAP, APOGEE) found, that is not supported. The first column is selected.
    apogee = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='APOGEE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'handietud'
        unique_together = (('numerohandicap', 'apogee'),)


class InscritModul(models.Model):
    id_modmat = models.OneToOneField('Module', models.DO_NOTHING, db_column='ID_MODMAT', primary_key=True)  # Field name made lowercase. The composite primary key (ID_MODMAT, APOGEE) found, that is not supported. The first column is selected.
    apogee = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='APOGEE')  # Field name made lowercase.
    annee = models.IntegerField(db_column='ANNEE', blank=True, null=True)  # Field name made lowercase.
    note_examen = models.IntegerField(db_column='NOTE_EXAMEN', blank=True, null=True)  # Field name made lowercase.
    resultat = models.IntegerField(db_column='RESULTAT', blank=True, null=True)  # Field name made lowercase.
    observaion = models.CharField(db_column='OBSERVAION', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscrit_modul'
        unique_together = (('id_modmat', 'apogee'),)


class Inscritbac(models.Model):
    apogee = models.OneToOneField(Etudiant, models.DO_NOTHING, db_column='APOGEE', primary_key=True)  # Field name made lowercase. The composite primary key (APOGEE, CODEBAC, IDETABLISSMENTBAC, ID_DETAIL) found, that is not supported. The first column is selected.
    codebac = models.ForeignKey(Bac, models.DO_NOTHING, db_column='CODEBAC')  # Field name made lowercase.
    idetablissmentbac = models.ForeignKey(Etablissementbac, models.DO_NOTHING, db_column='IDETABLISSMENTBAC')  # Field name made lowercase.
    id_detail = models.ForeignKey(DetailEnum, models.DO_NOTHING, db_column='ID_DETAIL')  # Field name made lowercase.
    id_detailprov = models.ForeignKey(DetailEnum, models.DO_NOTHING, db_column='ID_DETAILPROV', related_name='inscritbac_id_detailprov_set', blank=True, null=True)  # Field name made lowercase.
    annee = models.IntegerField(db_column='ANNEE', blank=True, null=True)  # Field name made lowercase.
    note = models.DecimalField(db_column='NOTE', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mention = models.CharField(db_column='MENTION', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscritbac'
        unique_together = (('apogee', 'codebac', 'idetablissmentbac', 'id_detail'),)


class Inscritdip(models.Model):
    codediplome = models.OneToOneField(Diplome, models.DO_NOTHING, db_column='CODEDIPLOME', primary_key=True)  # Field name made lowercase. The composite primary key (CODEDIPLOME, APOGEE, IDETABLISSEMENTBP) found, that is not supported. The first column is selected.
    apogee = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='APOGEE')  # Field name made lowercase.
    idetablissementbp = models.ForeignKey(Etablissementbp, models.DO_NOTHING, db_column='IDETABLISSEMENTBP')  # Field name made lowercase.
    annee = models.IntegerField(db_column='ANNEE', blank=True, null=True)  # Field name made lowercase.
    note = models.DecimalField(db_column='NOTE', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mention = models.CharField(db_column='MENTION', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscritdip'
        unique_together = (('codediplome', 'apogee', 'idetablissementbp'),)


class Intervenir(models.Model):
    idutilisateur = models.OneToOneField('utilisateur', models.DO_NOTHING, db_column='idutilisateur', primary_key=True)  # Field name made lowercase. The composite primary key (idutilisateur, ID_MODMAT) found, that is not supported. The first column is selected.
    id_modmat = models.ForeignKey('Module', models.DO_NOTHING, db_column='ID_MODMAT')  # Field name made lowercase.
    annee = models.IntegerField(db_column='ANNEE', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'intervenir'
        unique_together = (('idutilisateur', 'id_modmat'),)


class Langue(models.Model):
    id_langue = models.IntegerField(db_column='ID_LANGUE', primary_key=True)  # Field name made lowercase.
    intulite = models.CharField(db_column='INTULITE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'langue'


class Local(models.Model):
    id_local = models.IntegerField(db_column='ID_LOCAL', primary_key=True)  # Field name made lowercase.
    num_local = models.IntegerField(db_column='NUM_LOCAL', blank=True, null=True)  # Field name made lowercase.
    capacite = models.IntegerField(db_column='CAPACITE', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'local'


class ModFilSem(models.Model):
    id_modmat = models.OneToOneField('Module', models.DO_NOTHING, db_column='ID_MODMAT', primary_key=True)  # Field name made lowercase. The composite primary key (ID_MODMAT, ID_FILIERE, ID_SEMESTRE) found, that is not supported. The first column is selected.
    id_filiere = models.ForeignKey(Filiere, models.DO_NOTHING, db_column='ID_FILIERE')  # Field name made lowercase.
    id_semestre = models.ForeignKey('Semestre', models.DO_NOTHING, db_column='ID_SEMESTRE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mod_fil_sem'
        unique_together = (('id_modmat', 'id_filiere', 'id_semestre'),)


class Module(models.Model):
    id_modmat = models.CharField(db_column='ID_MODMAT', primary_key=True, max_length=30)  # Field name made lowercase.
    idutilisateur = models.ForeignKey('utilisateur', models.DO_NOTHING, db_column='idutilisateur')  # Field name made lowercase.
    intulite_ar = models.CharField(db_column='INTULITE_AR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intulite_fr = models.CharField(db_column='INTULITE_FR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    volume_horaire = models.IntegerField(db_column='VOLUME_HORAIRE', blank=True, null=True)  # Field name made lowercase.
    nbr_matiere = models.IntegerField(db_column='NBR_MATIERE', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_modupere = models.CharField(db_column='ID_MODUPERE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_modprerequi = models.CharField(db_column='ID_MODPREREQUI', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'module'


class ModuleLangue(models.Model):
    id_modmat = models.OneToOneField(Module, models.DO_NOTHING, db_column='ID_MODMAT', primary_key=True)  # Field name made lowercase. The composite primary key (ID_MODMAT, ID_LANGUE) found, that is not supported. The first column is selected.
    id_langue = models.ForeignKey(Langue, models.DO_NOTHING, db_column='ID_LANGUE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'module_langue'
        unique_together = (('id_modmat', 'id_langue'),)


class ModuleTypeEns(models.Model):
    id_modmat = models.OneToOneField(Module, models.DO_NOTHING, db_column='ID_MODMAT', primary_key=True)  # Field name made lowercase. The composite primary key (ID_MODMAT, ID_TYPES) found, that is not supported. The first column is selected.
    id_types = models.ForeignKey('TypeEnseigner', models.DO_NOTHING, db_column='ID_TYPES')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'module_type_ens'
        unique_together = (('id_modmat', 'id_types'),)


class ParcoursTypeDesciplin(models.Model):
    id_modmat = models.OneToOneField(Module, models.DO_NOTHING, db_column='ID_MODMAT', primary_key=True)  # Field name made lowercase. The composite primary key (ID_MODMAT, ID_DETAIL) found, that is not supported. The first column is selected.
    id_detail = models.ForeignKey(DetailEnum, models.DO_NOTHING, db_column='ID_DETAIL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parcours_type_desciplin'
        unique_together = (('id_modmat', 'id_detail'),)



class ProffessTypreside(models.Model):
    apogee = models.OneToOneField(Etudiant, models.DO_NOTHING, db_column='APOGEE', primary_key=True)  # Field name made lowercase. The composite primary key (APOGEE, ID_DETAIL) found, that is not supported. The first column is selected.
    id_detail = models.ForeignKey(DetailEnum, models.DO_NOTHING, db_column='ID_DETAIL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proffess_typreside'
        unique_together = (('apogee', 'id_detail'),)


class Reclamation(models.Model):
    id_reclamation = models.AutoField(db_column='ID_RECLAMATION', primary_key=True)  # Field name made lowercase.
    apogee = models.ForeignKey(Etudiant, models.DO_NOTHING, db_column='APOGEE')  # Field name made lowercase.
    id_modmat = models.ForeignKey(Module, models.DO_NOTHING, db_column='ID_MODMAT')  # Field name made lowercase.
    date_reclamation = models.DateField(db_column='DATE_RECLAMATION', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.TextField(db_column='COMMENTAIRE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reclamation'


class Semestre(models.Model):
    id_semestre = models.IntegerField(db_column='ID_SEMESTRE', primary_key=True)  # Field name made lowercase.
    intulite_semestre = models.CharField(db_column='INTULITE_SEMESTRE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'semestre'


class Specialite(models.Model):
    idspec = models.AutoField(db_column='IDSPEC', primary_key=True)  # Field name made lowercase.
    intitulespec = models.CharField(db_column='INTITULESPEC', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specialite'


class TypeEnseigner(models.Model):
    id_types = models.IntegerField(db_column='ID_TYPES', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type_enseigner'


class Universofpp(models.Model):
    idetablissementbp = models.OneToOneField(Etablissementbp, models.DO_NOTHING, db_column='IDETABLISSEMENTBP', primary_key=True)  # Field name made lowercase. The composite primary key (IDETABLISSEMENTBP, ID_DETAIL) found, that is not supported. The first column is selected.
    id_detail = models.ForeignKey(DetailEnum, models.DO_NOTHING, db_column='ID_DETAIL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'universofpp'
        unique_together = (('idetablissementbp', 'id_detail'),)


class Ville(models.Model):
    codepostal = models.IntegerField(db_column='CODEPOSTAL', primary_key=True)  # Field name made lowercase.
    id_detail = models.ForeignKey(DetailEnum, models.DO_NOTHING, db_column='ID_DETAIL', blank=True, null=True)  # Field name made lowercase.
    intituleville = models.CharField(db_column='INTITULEVILLE', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ville'