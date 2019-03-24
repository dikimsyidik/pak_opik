from django.dispatch import receiver
from django.utils.text import slugify

from django.utils import timezone
from datetime import timedelta, datetime, date
from django.db import models
from uuid import uuid4
import os
import random
import datetime
from django.contrib.auth.models import AbstractUser

PEKERJAAN = [
		('pns','PNS'),
		('pegawai swasta','Pegawai Swasta'),
		('wiraswasta','Wiraswasta'),
	]

def create_id():
    return str(uuid4())[:5]

# Create your models here.
class Kavling(models.Model):
	nama_kavling = models.CharField(max_length=100)
	hook =  models.IntegerField(default = 0)
	harga_standar = models.IntegerField(default=0)
	booking = models.IntegerField(default=0)
	uang_muka = models.IntegerField(default=0)
	klt =  models.FloatField(default = 0)
	biaya_strategis =  models.IntegerField(default = 0)
	slug            = models.SlugField(null=True, blank=True)
	plafon = models.IntegerField(default = 0)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug= slugify(self.nama_kavling)
		super(Kavling, self).save(*args, **kwargs)

	def __str__(self):
		return self.nama_kavling

def path_and_rename(instance, filename):
    return (str(instance)+".jpg")


class Kostumer(models.Model):
	''' diri'''
	nama = models.CharField(max_length=100)
	kavling = models.OneToOneField('Kavling',on_delete=models.CASCADE,primary_key=True,related_name='pemohon')
	no_ktp = models.CharField(max_length=30)
	tempat_lahir =   models.CharField(max_length=100)
	tanggal_lahir = models.DateField()
	alamat = models.CharField(max_length=100)
	no_hp = models.CharField(max_length=100)
	pekerjaan = models.CharField(max_length=100,blank=True,null=True,choices = PEKERJAAN)
	slug            = models.SlugField(null=True, blank=True)



	nama_perusahaan = models.CharField(max_length=100,blank=True,null=True)
	alamat_perusahaan = models.TextField(max_length=100,blank=True,null=True)
	nama_atasan = models.CharField(max_length=100,blank=True,null=True)
	no_hp_atasan = models.CharField(max_length=100,blank=True,null=True)



	timestamp       = models.DateTimeField(auto_now_add=True)

	''' pasangan '''
	nama_pasangan = models.CharField(max_length=100,blank=True,null=True)
	no_ktp_pasangan = models.CharField(max_length=30,blank=True,null=True)
	tempat_lahir_pasangan =   models.CharField(max_length=100,blank=True,null=True)
	tanggal_lahir_pasangan = models.CharField(max_length=10,blank=True,null=True)
	alamat_pasangan = models.TextField(max_length=100,blank=True,null=True)
	pekerjaan_pasangan = models.CharField(max_length=100,blank=True,null=True)
	no_hp_pasangan = models.CharField(max_length=100,blank=True,null=True)

	'''terdekat'''
	nama_keluarga = models.CharField(max_length=100,blank=True,null=True)
	no_ktp_keluarga = models.CharField(max_length=30,blank=True,null=True)
	alamat_keluarga = models.TextField(max_length=100,blank=True,null=True)
	no_hp_keluarga= models.CharField(max_length=100,blank=True,null=True)



	''' berkas '''
	ktp = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	kartu_keluarga = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	buku_nikah = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	npwp = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	keteranganpenghasilan = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	foto = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	rekening_koran = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	sk_bekerja = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	sliip_gaji = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	kartu_pegawai = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	sku_skhu = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	neraca = models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')
	foto_usaha =models.ImageField(blank=True,null=True, upload_to=path_and_rename,default='tidak_ada.jpg')


	'''progress'''
	dc = models.BooleanField(default=False)
	tanggal_dc = models.DateTimeField(blank=True,null=True)
	ket_dc = models.TextField(blank=True,null=True)

	slik =  models.BooleanField(default=False)
	tanggal_slik = models.DateTimeField(blank=True,null=True)
	ket_slik = models.TextField(blank=True,null=True)

	wawancara	= models.BooleanField(default=False)
	tanggal_wawancara = models.DateTimeField(blank=True,null=True)
	ket_wawancara = models.TextField(blank = True,null=True)

	ots= models.BooleanField(default=False)
	tanggal_ots = models.DateTimeField(blank=True,null=True)
	ket_ots = models.TextField(blank = True,null=True)

	sp3k= models.BooleanField(default=False)
	tanggal_sp3k = models.DateTimeField(blank=True,null=True)
	ket_sp3k = models.TextField(blank = True,null=True)

	akad= models.BooleanField(default=False)
	tanggal_akad = models.DateTimeField(blank=True,null=True)
	ket_akad = models.TextField(blank = True,null=True)

	jumlah = 0
	hasil =0


	# def penjumlahan(self):

	# 	return self.hasil

	def save(self, *args, **kwargs):
		self.jumlah = int(self.dc) + int(self.slik) + int(self.wawancara) + int(self.ots) + int(self.sp3k) + int(self.akad)
		self.hasil = self.jumlah / 6 * 100

		if self.dc and self.tanggal_dc is None:
			self.tanggal_dc = timezone.now()
		elif not self.dc and self.tanggal_dc is not None:
			self.tanggal_dc = None

		if self.slik and self.tanggal_slik is None:
			self.tanggal_slik = timezone.now()
		elif not self.slik and self.tanggal_slik is not None:
			self.tanggal_slik = None

		if self.wawancara and self.tanggal_wawancara is None:
			self.tanggal_wawancara = timezone.now()
		elif not self.wawancara and self.tanggal_wawancara is not None:
			self.tanggal_wawancara = None

		if self.ots and self.tanggal_ots is None:
			self.tanggal_ots = timezone.now()
		elif not self.ots and self.tanggal_ots is not None:
			self.tanggal_ots = None

		if self.sp3k and self.tanggal_sp3k is None:
			self.tanggal_sp3k = timezone.now()
		elif not self.sp3k and self.tanggal_sp3k is not None:
			self.tanggal_sp3k = None

		if self.akad and self.tanggal_akad is None:
			self.tanggal_akad = timezone.now()
		elif not self.akad and self.tanggal_akad is not None:
			self.tanggal_akad = None

		if not self.slug:
			self.slug= slugify(self.nama)
		super(Kostumer, self).save(*args, **kwargs)


	def __str__(self):
		return self.nama




class Marketer(models.Model):
	id = models.CharField(primary_key=True,max_length=100, default=create_id, editable=False)
	nama =  models.CharField(max_length=100)
	no_hp =  models.CharField(max_length=100)
	email =  models.EmailField(max_length=100)
	slug            = models.SlugField(null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug= slugify(self.nama)
		super(Marketer, self).save(*args, **kwargs)

	def __str__(self):
		return self.nama

class Kegiatan_Marketingnya(models.Model):
	marketer =  models.ForeignKey('Marketer',on_delete=models.CASCADE, blank=True,null=True)
	judul_kegiatan =  models.CharField(max_length=100)
	deskripsi =  models.TextField()
	waktu = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.judul_kegiatan






@receiver(models.signals.post_delete, sender=Kostumer)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.ktp:
        if os.path.isfile(instance.ktp.path):
            os.remove(instance.ktp.path)




