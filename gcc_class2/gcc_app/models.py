# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


class Schedule(models.Model):
    coursetitle = models.CharField(db_column='courseTitle', max_length=32)  # Field name made lowercase.
    schoolyear = models.CharField(db_column='schoolYear', max_length=10, blank=True, null=True)  # Field name made lowercase.
    schoolterm = models.CharField(db_column='schoolTerm', max_length=5, blank=True, null=True)  # Field name made lowercase.
    teacher = models.CharField(max_length=10, blank=True, null=True)
    courseid = models.CharField(db_column='courseId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    coursesection = models.CharField(db_column='courseSection', max_length=15, blank=True, null=True)  # Field name made lowercase.
    courseweek = models.CharField(db_column='courseWeek', max_length=15, blank=True, null=True)  # Field name made lowercase.
    campus = models.CharField(max_length=15, blank=True, null=True)
    courseroom = models.CharField(db_column='courseRoom', max_length=15, blank=True, null=True)  # Field name made lowercase.
    classname = models.CharField(db_column='className', max_length=60, blank=True, null=True)  # Field name made lowercase.
    hourscomposition = models.CharField(db_column='hoursComposition', max_length=25, blank=True, null=True)  # Field name made lowercase.
    weeklyhours = models.CharField(db_column='weeklyHours', max_length=5, blank=True, null=True)  # Field name made lowercase.
    totalhours = models.CharField(db_column='totalHours', max_length=5, blank=True, null=True)  # Field name made lowercase.
    credit = models.CharField(max_length=5, blank=True, null=True)
    users = models.ForeignKey('UsersAccountInfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        managed = True
        db_table = 'schedule'


class Score(models.Model):
    user_id = models.CharField(max_length=50)

    class Meta:
        # managed = False
        managed = True
        db_table = 'score'


class UsersAccountInfo(models.Model):
    studentid = models.CharField(db_column='studentId', unique=True, max_length=32)  # Field name made lowercase.
    passwd = models.CharField(max_length=32)
    user_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        # managed = False
        managed = True
        db_table = 'users_account_info'


class UsersInfo(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    studentid = models.CharField(db_column='studentId', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    brithday = models.DateField(blank=True, null=True)
    idnumber = models.CharField(db_column='idNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    candidatenumber = models.CharField(db_column='candidateNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=10, blank=True, null=True)
    collegename = models.CharField(db_column='collegeName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    majorname = models.CharField(db_column='majorName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    classname = models.CharField(db_column='className', max_length=32, blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateField(db_column='entryDate', blank=True, null=True)  # Field name made lowercase.
    domicile = models.CharField(max_length=32, blank=True, null=True)
    politicalstatus = models.CharField(db_column='politicalStatus', max_length=32, blank=True, null=True)  # Field name made lowercase.
    national = models.CharField(max_length=15, blank=True, null=True)
    education = models.CharField(max_length=15, blank=True, null=True)
    users = models.ForeignKey(UsersAccountInfo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        managed = True
        db_table = 'users_info'
