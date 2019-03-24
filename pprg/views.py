from __future__ import print_function
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from .models import Kostumer,Kavling,Marketer
from django.db.models import Q
from django.http import HttpResponseRedirect,HttpResponse
from django.core.files import File
from .forms import TambahKostumerForm,EditKostumerForm,TambahKavlingForm,TambahMarketerForm,KegiatanForm
from mailmerge import MailMerge
from datetime import date,datetime,timedelta
from io import StringIO
from django.contrib.auth.decorators import user_passes_test 
import os
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

def email_check(user):
    return user.email.endswith('@pprg.com')

BASE = os.path.dirname(os.path.abspath(__file__))

def path_and_rename(instance, filename):
    return (str(instance)+".docx")
# Create your views here.

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def dashboard(request):

	query = request.GET.get("q", None)
	qs = Kostumer.objects.filter(pekerjaan='pns').order_by('-timestamp')

	tanggal = datetime.now()
	if query is not None:
		qs = qs.filter(
                Q(nama__icontains=query)
                )
	template = 'dashboard_pprg/index.html'
	context = {
			'list_kostumer':qs,
			'tanggal':tanggal,
			}

	return render(request,template,context)

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def list_swasta(request):
	query = request.GET.get("q", None)
	qs = Kostumer.objects.filter(pekerjaan='pegawai swasta').order_by('-timestamp')
	if query is not None:
		qs = qs.filter(
                Q(nama__icontains=query)
                )
	template = 'dashboard_pprg/list_swasta.html'
	context = {
			'list_kostumer':qs
			}

	return render(request,template,context)
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def list_wiraswasta(request):
	query = request.GET.get("q", None)
	qs = Kostumer.objects.filter(pekerjaan='wiraswasta').order_by('-timestamp')
	if query is not None:
		qs = qs.filter(
                Q(nama__icontains=query)
                )
	template = 'dashboard_pprg/list.wiraswasta.html'
	context = {
			'list_kostumer':qs
			}

	return render(request,template,context)



@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def tambah_kostumer(request):
	template = 'dashboard_pprg/tambahkonsumen-pns.html'
	form = TambahKostumerForm(request.POST,request.FILES or None)
	if request.method == 'POST':
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/pprg/')
	context = {
		'form':form
	}

	return render(request,template,context)

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def tambah_peg_swasta(request):
	template = 'dashboard_pprg/tambahkonsumen-swasta.html'
	form = TambahKostumerForm(request.POST,request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/pprg/list_swasta/')
	context = {
		'form':form
	}

	return render(request,template,context)
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def tambah_wiraswasta(request):
	template = 'dashboard_pprg/tambahkonsumen-wiraswasta.html'
	form = TambahKostumerForm(request.POST,request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/pprg/list_wiraswasta/')
	context = {
		'form':form
	}

	return render(request,template,context)

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def edit_kostumer_pns(request,slug=None):
	obj = get_object_or_404(Kostumer,slug=slug)
	form = EditKostumerForm(request.FILES or None, instance=obj)
	context = {"form": form,'obj':obj}
	if request.method == 'POST':
		form = EditKostumerForm(request.POST,request.FILES or None, instance=obj)
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect("/pprg/")
	template = "dashboard_pprg/edit-pns.html"
	return render(request, template, context)

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def edit_kostumer_swasta(request,slug=None):
	obj = get_object_or_404(Kostumer,slug=slug)
	form = EditKostumerForm(request.FILES or None, instance=obj)
	context = {"form": form,'obj':obj}
	if request.method == 'POST':
		form = EditKostumerForm(request.POST,request.FILES or None, instance=obj)

		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect("/pprg/list_swasta/")
	template = "dashboard_pprg/edit-swasta.html"
	return render(request, template, context)


@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def edit_kostumer_wiraswasta(request,slug=None):
	obj = get_object_or_404(Kostumer,slug=slug)
	form = EditKostumerForm(request.FILES or None, instance=obj)
	context = {"form": form,'obj':obj}
	if request.method == 'POST':
		form = EditKostumerForm(request.POST,request.FILES or None, instance=obj)

		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect("/pprg/list_wiraswasta/")
	template = "dashboard_pprg/edit-wiraswasta.html"
	return render(request, template, context)





@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def data_kavling(request):
	kavling = Kavling.objects.all().order_by('nama_kavling')

	query = request.GET.get("q", None)
	qs = Kavling.objects.all().order_by('nama_kavling')



	if query is not None:
		qs = qs.filter(
                Q(nama__icontains=query)
                )
	template = 'dashboard_pprg/kavling.html'
	context = {
			'list_kavling':qs
			}

	return render(request,template,context)
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def tambah_kavling(request):
	template = 'dashboard_pprg/kavlingform.html'
	form = TambahKavlingForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/pprg/kavling')
	context = {
		'form':form
	}

	return render(request,template,context)

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def edit_kavling(request,slug = None):
	template = 'dashboard_pprg/kavlingform.html'
	obj = get_object_or_404(Kavling,slug=slug)
	total = obj.hook + obj.harga_standar + obj.klt+ obj.biaya_strategis
	form = TambahKavlingForm(request.POST or None,instance=obj)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/pprg/kavling/')
	context = {
		'form':form,
		'total':total,
		'obj':obj,
	}

	return render(request,template,context)



@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def list_marketer(request):
	marketer = Marketer.objects.all()

	query = request.GET.get("q", None)
	qs = Marketer.objects.all()
	if query is not None:
		qs = qs.filter(
                Q(nama__icontains=query)
                )
	template = 'dashboard_pprg/list_marketer.html'
	context = {
			'list_marketer':qs
			}

	return render(request,template,context)

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def tambah_marketer(request):
	template = 'dashboard_pprg/marketertambah.html'
	form = TambahMarketerForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/pprg/marketer/')
	context = {
		'form':form
	}

	return render(request,template,context)

def kegiatan_marketing(request):
	template = 'dashboard_pprg/marketer.html'
	form = KegiatanForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return HttpResponseRedirect('/')
	context = {
		'form':form
	}

	return render(request,template,context)

def laporan_marketing(request,slug=None):
	obj = get_object_or_404(Marketer,slug = slug)
	print(obj.kegiatan_marketingnya_set.all())
	kegiatan = obj.kegiatan_marketingnya_set.all()
	template = 'dashboard_pprg/marketerlaporan.html'
	context = {
		'obj':obj,
		'kegiatan':kegiatan,
	}

	return render(request,template,context)







@login_required
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def flpp_print(request,slug = None):
	obj = get_object_or_404(Kostumer,slug=slug)
	file = os.path.join(BASE,'flpp.docx')

	document = MailMerge(file)
	tanggal = str(date.today())
	tang = obj.tanggal_lahir
	tanggal_lahir = tang.strftime('%d-%m-%Y')
	tgl_str = obj.tanggal_lahir_pasangan
	datetime_object = datetime.strptime(tgl_str, '%m/%d/%Y')
	tanggal_lahir_pasangan = datetime_object.strftime('%d-%m-%Y')
	# lahir_pasangan = tanggal_lahir_pasangan.strftime('%d-%m-%Y')

	document.merge(Nama_PT='PT Mitra Budiman Propertido',
 		TTL_Pemohon=obj.tempat_lahir +' '+ tanggal_lahir,
 		Nama_Perumahan='PPRG',
 		No_KTP_IstriSuami=obj.no_ktp_pasangan,
 		Alamat_Pemohon=obj.alamat,
 		Nama_Pemohon=obj.nama,
 		Alamat_SuamiIstri=obj.alamat_pasangan,
 		Nama_Direktur='',
 		TTL_IstriSuami=obj.tempat_lahir_pasangan +' '+tanggal_lahir_pasangan,
 		Pekerjaan_Pemohon_=obj.pekerjaan,
 		No_KTP_Pemohon=obj.no_ktp,
 		Nama_IstriSuami=obj.nama_pasangan,
 		Pekerjaan_Suamiistri=obj.pekerjaan_pasangan,
 		Alamat_Keluarga = obj.alamat_keluarga,
 		No_Ktp_Keluarga = obj.no_ktp_keluarga,
 		No_Handphone_Keluarga = obj.no_hp_keluarga,
 		Nama_Keluarga_Terdekat =obj.nama_keluarga,)



	path = document.write(os.path.join(settings.MEDIA_ROOT,'hasil/{}{}.docx'.format(obj.slug,tanggal)))
	context = {
			'nama_file':obj.slug,
			'tanggal':tanggal
	}

	return render(request,'dashboard_pprg/cetak.html',context)

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def sphj_print(request,slug = None):
	obj = get_object_or_404(Kostumer,slug=slug)
	file = os.path.join(BASE,'sphj.docx')
	dp = obj.kavling.uang_muka
	document = MailMerge(file)
	tanggal = str(date.today())

	tanggal_satu = date.today()
	tanggal_1 = tanggal_satu + timedelta(days=7)
	tanggal_2 = tanggal_satu + timedelta(days=14)
	tanggal_3 = tanggal_satu + timedelta(days=21)
	tanggal_4 = tanggal_satu + timedelta(days=28)
	sisa = obj.kavling.harga_standar +obj.kavling.klt - 123000000
	nilai = sisa/4

	document.merge(nama_pt='PT Mitra Budiman Propertido',
 		nama=obj.nama,
 		alamat=obj.alamat,
 		kavling= str(obj.kavling),
 		harga_standar=str(int(obj.kavling.harga_standar)),
 		uang_muka = str(int(obj.kavling.uang_muka)),
 		uang_booking = str(int(obj.kavling.booking)),
 		klt = str(int(obj.kavling.klt)),
 		hook = str(int(obj.kavling.hook)),
 		harga_jual= str(int(obj.kavling.harga_standar+obj.kavling.klt)),
 		total_harga = str(int(obj.kavling.harga_standar +obj.kavling.klt +obj.kavling.hook+obj.kavling.booking)),
 		telah_dibayar = str(int(obj.kavling.harga_standar +obj.kavling.klt +obj.kavling.hook +obj.kavling.booking)),
 		ajuan = str(obj.kavling.plafon),
 		sisa_harus_bayar = str(int(obj.kavling.harga_standar +obj.kavling.klt +obj.kavling.hook - obj.kavling.plafon)),
 		tanggal_now = str(tanggal),

 		)


	path = document.write(os.path.join(settings.MEDIA_ROOT,'hasil/{}{}.docx'.format(obj.slug,tanggal)))
	context = {
			'obj':obj,
			'dp':dp,
			'nama_file':obj.slug,
			'tanggal':tanggal}
	tanggal = date.today()


	return render(request,'dashboard_pprg/kwitansi2.html',context)



@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def laporan(request):
	kostumer = Kostumer.objects.all().order_by('-timestamp')
	tanggal = str(date.today())

	context = {
		'kostumer':kostumer,
		'tanggal':tanggal,


	}

	return render(request,'dashboard_pprg/laporan1.html',context)

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def progress(request):
	kostumer = Kostumer.objects.all().order_by('sliip_gaji')
	tanggal = str(date.today())

	context = {
		'list_kostumer':kostumer,
		'tanggal':tanggal,


	}

	return render(request,'dashboard_pprg/dokumen_danprogress.html',context)
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def progress2(request):
	kostumer = Kostumer.objects.all().order_by('-tanggal_akad')
	tanggal = str(date.today())


	persentasi = 0

	context = {
		'list_kostumer':kostumer,
		'tanggal':tanggal,
		'persentasi':persentasi,



	}

	return render(request,'dashboard_pprg/progress.html',context)

@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def rekap_akad(request):
	kavling = Kavling.objects.count()



	kostumer = Kostumer.objects.count()
	akad = Kostumer.objects.filter(akad=True).count()
	sp3k = Kostumer.objects.filter(sp3k=True).count()
	ots = Kostumer.objects.filter(ots=True).count()
	wawancara = Kostumer.objects.filter(wawancara=True).count()
	slik = Kostumer.objects.filter(slik=True).count()
	dc = Kostumer.objects.filter(dc=True).count()

	tahun = datetime.today().year
	print(tahun)
	januari = 1
	februari = 2
	maret = 3
	april =  4
	mei = 5
	juni = 6
	juli =  7
	agustus =8
	september =9
	oktober = 10
	november = 11
	desember = 12
	b  = Kostumer.objects

	tahun_akad = b.filter(tanggal_akad__year__gte=tahun)
	bulan_januari = b.filter(tanggal_akad__month__gte=januari).count()
	februari = b.filter(tanggal_akad__month__gte=februari).count()
	maret = b.filter(tanggal_akad__month__gte=maret).count()
	april = b.filter(tanggal_akad__month__gte=april).count()
	mei = b.filter(tanggal_akad__month__gte=mei).count()
	juni =b.filter(tanggal_akad__month__gte=juni).count()
	juli = b.filter(tanggal_akad__month__gte=juli).count()
	agustus = b.filter(tanggal_akad__month__gte=agustus).count()
	september = b.filter(tanggal_akad__month__gte=september).count()
	oktober = b.filter(tanggal_akad__month__gte=oktober).count()
	november =b.filter(tanggal_akad__month__gte=november).count()
	desember =b.filter(tanggal_akad__month__gte=desember).count()

	# peprbulan = {'januari'}
	print(maret)


	print(bulan_januari)
	akad_tahun = Kostumer.objects.dates('tanggal_akad','year')
	print(akad)


	k = Kostumer.objects.filter(tanggal_akad__year__gte=2019)
	tahun_nya = Kostumer.objects.filter(akad = True)
	objeknya = tahun_nya




	tanggal = date.today()


	context = {
		'kavling':kavling,
		'list_kostumer':kostumer,
		'tanggal':tanggal,
		'kostumer':kostumer,
		'akad':akad,
		'sp3k':sp3k,
		'ots':ots,
		'wawancara':wawancara,
		'slik':slik,
		'dc':dc,
		'tanggal':tanggal,
		'bulan_januari':bulan_januari,
		'bulan_januari':bulan_januari,
		'februari':februari,
		'maret':maret,
		'april':april,
		'mei':mei,
		'juni':juni,
		'juli':juli,
		'agustus':agustus,
		'september':september,
		'oktober':oktober,
		'november':november,
		'desember':desember,

	}

	return render(request,'dashboard_pprg/rekap_akad.html',context)



@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def hapus_kostumer(request,slug):
	data = get_object_or_404(Kostumer,slug=slug)
	data.delete()
	return HttpResponseRedirect('/pprg/dokumen_dan_progress/')
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def hapus_kavling(request,slug):
	data = get_object_or_404(Kavling,slug=slug)
	data.delete()
	return HttpResponseRedirect('/pprg/kavling/')
@user_passes_test(lambda u:u.is_superuser or u.email.endswith('@pprg.com'))
def hapus_marketer(request,slug):
	data = get_object_or_404(Marketer,slug=slug)
	data.delete()
	return HttpResponseRedirect('/pprg/marketer/')

