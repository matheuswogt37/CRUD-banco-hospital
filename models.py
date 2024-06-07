# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acompanhante(models.Model):
    id_pk = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=70, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    numero_telefone = models.CharField(max_length=12, blank=True, null=True)
    relacao = models.CharField(max_length=50, blank=True, null=True)
    id_internado_fk = models.ForeignKey('Internado', models.DO_NOTHING, db_column='id_internado_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acompanhante'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Cirurgia(models.Model):
    id_pk = models.AutoField(primary_key=True)
    descricao_cirurgia = models.TextField(blank=True, null=True)
    log_cirurgia = models.TextField(blank=True, null=True)
    data_cirurgia = models.DateField(blank=True, null=True)
    id_acompanhante_fk = models.ForeignKey(Acompanhante, models.DO_NOTHING, db_column='id_acompanhante_fk', blank=True, null=True)
    id_medico_fk = models.ForeignKey('Medico', models.DO_NOTHING, db_column='id_medico_fk', blank=True, null=True)
    id_paciente_fk = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente_fk', blank=True, null=True)
    id_enfermeira_fk = models.ForeignKey('Enfermeira', models.DO_NOTHING, db_column='id_enfermeira_fk', blank=True, null=True)
    id_sala_fk = models.ForeignKey('Sala', models.DO_NOTHING, db_column='id_sala_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cirurgia'


class Consulta(models.Model):
    id_pk = models.AutoField(primary_key=True)
    data_e_hora = models.DateTimeField(blank=True, null=True)
    id_paciente_fk = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente_fk', blank=True, null=True)
    id_medico_fk = models.ForeignKey('Medico', models.DO_NOTHING, db_column='id_medico_fk', blank=True, null=True)
    id_sala_fk = models.ForeignKey('Sala', models.DO_NOTHING, db_column='id_sala_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Enfermeira(models.Model):
    id_pk = models.AutoField(primary_key=True)
    coren = models.CharField(max_length=20, blank=True, null=True)
    nome = models.CharField(max_length=70, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    id_setor_fk = models.ForeignKey('Setor', models.DO_NOTHING, db_column='id_setor_fk', blank=True, null=True)
    id_telefone_fk = models.ForeignKey('Telefone', models.DO_NOTHING, db_column='id_telefone_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enfermeira'


class Internado(models.Model):
    id_pk = models.AutoField(primary_key=True)
    data_e_hora_entrada = models.DateTimeField(blank=True, null=True)
    data_e_hora_saida = models.DateTimeField(blank=True, null=True)
    id_sala_fk = models.ForeignKey('Sala', models.DO_NOTHING, db_column='id_sala_fk', blank=True, null=True)
    id_paciente_fk = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente_fk', blank=True, null=True)
    id_medico_fk = models.ForeignKey('Medico', models.DO_NOTHING, db_column='id_medico_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internado'


class LogAcompanhante(models.Model):
    id_pk = models.AutoField(primary_key=True)
    data_e_hora_entrada = models.DateTimeField(blank=True, null=True)
    data_e_hora_saida = models.DateTimeField(blank=True, null=True)
    id_acompanhante_fk = models.ForeignKey(Acompanhante, models.DO_NOTHING, db_column='id_acompanhante_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_acompanhante'


class Medicamentos(models.Model):
    id_pk = models.AutoField(primary_key=True)
    nome_generico = models.CharField(max_length=70, blank=True, null=True)
    nome_comercial = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    preco_unit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamentos'


class Medico(models.Model):
    id_pk = models.AutoField(primary_key=True)
    crm = models.CharField(max_length=12, blank=True, null=True)
    nome = models.CharField(max_length=70, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    id_sala_fk = models.ForeignKey('Sala', models.DO_NOTHING, db_column='id_sala_fk', blank=True, null=True)
    id_telefone_fk = models.ForeignKey('Telefone', models.DO_NOTHING, db_column='id_telefone_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'


class Paciente(models.Model):
    id_pk = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    id_telefone_fk = models.ForeignKey('Telefone', models.DO_NOTHING, db_column='id_telefone_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class RecMed(models.Model):
    id_pk = models.AutoField(primary_key=True)
    orientacao = models.CharField(max_length=150, blank=True, null=True)
    id_receita_fk = models.ForeignKey('Receita', models.DO_NOTHING, db_column='id_receita_fk', blank=True, null=True)
    id_medicamento_fk = models.ForeignKey(Medicamentos, models.DO_NOTHING, db_column='id_medicamento_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rec_med'


class Receita(models.Model):
    id_pk = models.AutoField(primary_key=True)
    id_consulta_fk = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='id_consulta_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receita'


class Sala(models.Model):
    id_pk = models.AutoField(primary_key=True)
    numero = models.IntegerField(blank=True, null=True)
    id_setor_fk = models.ForeignKey('Setor', models.DO_NOTHING, db_column='id_setor_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sala'


class Setor(models.Model):
    id_pk = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=True, null=True)
    funcao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setor'


class SetorSetor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    funcao = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'setor_setor'


class Telefone(models.Model):
    id_pk = models.AutoField(primary_key=True)
    celular = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefone'


class Visitante(models.Model):
    id_pk = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70, blank=True, null=True)
    data_e_hora_entrada = models.DateTimeField(blank=True, null=True)
    data_e_hora_saida = models.DateTimeField(blank=True, null=True)
    id_internado_fk = models.ForeignKey(Internado, models.DO_NOTHING, db_column='id_internado_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visitante'
