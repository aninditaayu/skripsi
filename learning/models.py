from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

#UserProfileKey
class UserProfileKey(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())
      
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'


#Bab
class Bab(models.Model):
    nama = models.CharField(max_length=128, unique=True)
    deskripsi = models.TextField(null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.nama)
            super(Bab, self).save(*args, **kwargs)
    
    def __unicode__(self):  
        return self.nama    

    class Meta:
        verbose_name_plural = "Bab"

#Materi
class Materi(models.Model):
    bab = models.ForeignKey(Bab, related_name="bab")
    judul_materi = models.CharField(max_length=128)
    deskripsi = models.TextField(null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.judul_materi)
            super(Materi, self).save(*args, **kwargs)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return "{}-{}".format(self.judul_materi, self.bab)

#Soal
class Soal(models.Model):
    materi = models.ForeignKey(Materi,related_name="materi")
    judul_soal = models.CharField(max_length=128)
    deskripsi_soal = models.TextField(null=False)
    instruksi = models.TextField(null=False)
    kunci_jawaban = models.TextField(null=False)
    hint = models.TextField(null=False)
    isi_console = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return "{}-{}".format(self.judul_soal, self.materi)

#Jawaban
class Jawaban(models.Model):
    soal = models.ForeignKey(Soal)
    user = models.ForeignKey(User)
    jawaban = models.TextField()
    console_user = models.TextField(null = True, blank=True)
    waktu_jawab = models.DateTimeField(auto_now_add=True)
    kali_jawab = models.IntegerField(default=0)
    sudah_benar = models.BooleanField(default=False)

    def __unicode__(self):
        return "Soal {0} - {1} - {2}".format(self.soal, self.user, self.kali_jawab)

