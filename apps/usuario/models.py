from django.db import models

# Create your models here.

class Introduction(models.Model):
    id = models.AutoField(primary_key = True)
    about = models.CharField('About',max_length = 300, null = False, blank = False)
    intro = models.TextField(blank = False, null = False)
    active = models.BooleanField('active', default = False)

    class Meta:
        verbose_name = 'Introduction'
        verbose_name_plural = 'Introductions'
        ordering = ['id']

    def __str__(self):
        return self.intro

class Accomplishments(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length = 200, null = False, blank = False)
    description = models.TextField(null = False, blank = False)

    class Meta:
        verbose_name = 'Accomplishment'
        verbose_name_plural = 'Accomplishment'
        ordering = ['name']

    def __str__(self):
        return self.name

class Experience(models.Model):
    id = models.AutoField(primary_key = True)
    job = models.CharField('Job', max_length = 300, null = False, blank = False)
    place = models.CharField('Place', max_length = 300, null = False, blank = False)
    zone = models.CharField('Zone', max_length = 300, null = False, blank = False)
    resume = models.TextField(blank = False, null = False)
    startdate = models.DateField('Fecha de inicio')
    enddate = models.DateField('Fecha de termino', null = True, blank = True)
    accomplish = models.ManyToManyField(Accomplishments)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'
        ordering = ['job']

    def __str__(self):
        return self.job

class Degree(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Degree',max_length = 200, null = False, blank = False)

    class Meta:
        verbose_name = 'Degree'
        verbose_name_plural = 'Degrees'
        ordering = ['name']

    def __str__(self):
        return self.name

class Education(models.Model):
    id = models.AutoField(primary_key = True)
    degree = models.ForeignKey(Degree, default = 1 ,on_delete = models.CASCADE)
    place = models.CharField('Place', max_length = 200, null = False, blank = False)
    area = models.CharField('Major', max_length = 200, null = False, blank = False)
    special = models.CharField('Speciality', max_length = 200, null = False, blank = False)
    startdate = models.DateField('Fecha de inicio')
    enddate = models.DateField('Fecha de termino')

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
        ordering = ['place']

    def __str__(self):
        return self.place

class SoftSkill(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Name',max_length = 200, null = False, blank = False)

    class Meta:
        verbose_name = 'SoftSkill'
        verbose_name_plural = 'SoftSkills'
        ordering = ['name']

    def __str__(self):
        return self.name

class Language(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length = 100, null = False, blank = False)
    percent = models.CharField('Percent', max_length = 4, null = False, blank = False)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['name']

    def __str__(self):
        return self.name

class Skill(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length = 100, null = False, blank = False)
    percent = models.CharField('Percent', max_length = 4, null = False, blank = False)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['name']

    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.AutoField(primary_key = True)
    phone = models.CharField('Phone', max_length = 15, null = False, blank = False)
    mail = models.EmailField('Direccion de correo', blank = False, null = False)
    linkedIn = models.URLField('LinkedIn', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    address = models.CharField('Address', max_length = 200, null = False, blank = False)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['phone']

    def __str__(self):
        return self.phone

class GeneralInfo(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length = 200, null = False, blank = False)
    birth = models.DateField('Birth')
    city = models.CharField('City', max_length = 200, null = False, blank = False)
    me = models.URLField(max_length = 255, blank = True, null = True)

    class Meta:
        verbose_name = 'GeneralInfo'
        verbose_name_plural = 'GeneralInfo'
        ordering = ['name']

    def __str__(self):
        return self.name
