from django import forms
from .models import Kostumer,Kavling,Marketer,Kegiatan_Marketingnya
PEKERJAAN = [
		('pns','PNS'),
		('pegawai swasta','Pegawai Swasta'),
		('wiraswasta','Wiraswasta'),
	]

class EditKostumerForm(forms.ModelForm):
	class Meta:
		model = Kostumer
		fields = [
			'nama',
			'kavling',
			'no_ktp',
			'tempat_lahir',
			'tanggal_lahir',
			'alamat',
			'no_hp',
			'pekerjaan',
			'nama_perusahaan',
			'alamat_perusahaan',
			'nama_atasan',
			'no_hp_atasan',
			'nama_pasangan',
			'no_ktp_pasangan',
			'tempat_lahir_pasangan',
			'tanggal_lahir_pasangan',
			'alamat_pasangan',
			'pekerjaan_pasangan',
			'no_hp_pasangan',
			'nama_keluarga',
			'no_ktp_keluarga',
			'alamat_keluarga',
			'no_hp_keluarga',
			'ktp',
			'kartu_keluarga',
			'buku_nikah',
			'npwp',
			'keteranganpenghasilan',
			'foto',
			'rekening_koran',
			'sk_bekerja',
			'sliip_gaji',
			'kartu_pegawai',
			'sku_skhu',
			'neraca',
			'foto_usaha',
			'dc',
			'slik',
			'wawancara',
			'ots',
			'sp3k',
			'akad',
			'ket_dc',
			'ket_slik',
			'ket_wawancara',
			'ket_ots',
			'ket_sp3k',
			'ket_akad',]
		def __init__(self):
			pass
		widgets = {
			'kavling':forms.Select(attrs={'class': ''}),
			'nama':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'tanggal_lahir':forms.TextInput(attrs={'class': 'form-control datepicker','value':'10/20/1970','placeholder':'Pilih Tanggal'}),
			'no_ktp':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'tempat_lahir':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'alamat':forms.Textarea(attrs={'class': 'form-control','placeholder':'Nama'}),
			'pekerjaan':forms.Select(attrs={'class': 'form-control','choices':PEKERJAAN}),
			'no_hp':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),

			'nama_perusahaan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama Perusahaan'}),
			'alamat_perusahaan':forms.TextInput(attrs={'class':'form-control','placeholder':'Alamat Perusahaan '}),
			'nama_atasan':forms.TextInput(attrs={'class':'form-control','placeholder':'Nama Atasan'}),
			'no_hp_atasan':forms.TextInput(attrs={'class':'form-control','placeholder':'No HP Atasan'}),


			'nama_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'tanggal_lahir_pasangan':forms.TextInput(attrs={'class': 'form-control datepicker','value':'10/20/1970','placeholder':'Pilih Tanggal'}),
			'no_ktp_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'tempat_lahir_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'alamat_pasangan':forms.Textarea(attrs={'class': 'form-control','placeholder':'Nama'}),
			'pekerjaan_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_hp_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),

			'nama_keluarga':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_ktp_keluarga':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'alamat_keluarga':forms.Textarea(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_hp_keluarga':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),

			'ktp':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'kartu_keluarga':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'buku_nikah':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload' }),
			'npwp':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'keteranganpenghasilan':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'foto':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'rekening_koran':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'sk_bekerja':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'sliip_gaji':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'kartu_pegawai':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'sku_skhu':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'neraca':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'foto_usaha':forms.FileInput(attrs={'class': 'fileupload','name':'fileupload'}),
			'dc':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck1'}),
			'slik':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck2'}),
			'wawancara':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck3'}),
			'ots':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck4'}),
			'sp3k':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck5'}),
			'akad':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck6'}),
			'ket_dc':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_slik':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_wawancara':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_ots':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_sp3k':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_akad':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),


		}


class TambahKostumerForm(forms.ModelForm):
	class Meta:
		model = Kostumer
		fields = [
			'nama',
			'kavling',
			'no_ktp',
			'tempat_lahir',
			'tanggal_lahir',
			'alamat',
			'no_hp',
			'pekerjaan',
			'nama_perusahaan',
			'alamat_perusahaan',
			'nama_atasan',
			'no_hp_atasan',
			'nama_pasangan',
			'no_ktp_pasangan',
			'tempat_lahir_pasangan',
			'tanggal_lahir_pasangan',
			'alamat_pasangan',
			'pekerjaan_pasangan',
			'no_hp_pasangan',
			'nama_keluarga',
			'no_ktp_keluarga',
			'alamat_keluarga',
			'no_hp_keluarga',
			'ktp',
			'kartu_keluarga',
			'buku_nikah',
			'npwp',
			'keteranganpenghasilan',
			'foto',
			'rekening_koran',
			'sk_bekerja',
			'sliip_gaji',
			'kartu_pegawai',
			'sku_skhu',
			'neraca',
			'foto_usaha',
			'dc',
			'slik',
			'wawancara',
			'ots',
			'sp3k',
			'akad',
			'ket_dc',
			'ket_slik',
			'ket_wawancara',
			'ket_ots',
			'ket_sp3k',
			'ket_akad',
			]
		def __init__(self):
			pass
		widgets = {
			'kavling':forms.Select(attrs={'class': 'form-control'}),
			'nama':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'tanggal_lahir':forms.TextInput(attrs={'class': 'form-control datepicker','value':'10/20/1970','placeholder':'Pilih Tanggal'}),
			'no_ktp':forms.TextInput(attrs={'class': 'form-control','placeholder':'No Ktp'}),
			'tempat_lahir':forms.TextInput(attrs={'class': 'form-control','placeholder':'Tempat Lahir'}),
			'alamat':forms.Textarea(attrs={'class': 'form-control','placeholder':'Alamat'}),
			'no_hp':forms.TextInput(attrs={'class': 'form-control','placeholder':'No HP'}),
			'pekerjaan':forms.Select(attrs={'class': 'form-control','value':'PNS'}),
			'nama_perusahaan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama Perusahaan'}),
			'alamat_perusahaan':forms.Textarea(attrs={'class':'form-control','placeholder':'Alamat Perusahaan '}),
			'nama_atasan':forms.TextInput(attrs={'class':'form-control','placeholder':'Nama Atasan'}),
			'no_hp_atasan':forms.TextInput(attrs={'class':'form-control','placeholder':'No HP Atasan'}),
			'nama_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama Pasangan'}),
			'tanggal_lahir_pasangan':forms.TextInput(attrs={'class': 'form-control datepicker','value':'10/20/1970','placeholder':'Pilih Tanggal'}),
			'no_ktp_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'No KTP Pasangan'}),
			'tempat_lahir_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'alamat_pasangan':forms.Textarea(attrs={'class': 'form-control','placeholder':'Alamat Pasangan'}),
			'pekerjaan_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Pekerjaan Pasangan'}),
			'no_hp_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'No Hp Pasangan'}),

			'nama_keluarga':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_ktp_keluarga':forms.TextInput(attrs={'class': 'form-control','placeholder':'No KTP'}),
			'alamat_keluarga':forms.Textarea(attrs={'class': 'form-control','placeholder':'Alamat '}),
			'no_hp_keluarga':forms.TextInput(attrs={'class': 'form-control','placeholder':'No HP'}),

			'ktp':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'kartu_keluarga':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'buku_nikah':forms.FileInput(attrs={'class': 'dropify','name':'dropify' }),
			'npwp':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'keteranganpenghasilan':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'foto':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'rekening_koran':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'sk_bekerja':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'sliip_gaji':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'kartu_pegawai':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'sku_skhu':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'neraca':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'foto_usaha':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'dc':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck1'}),
			'slik':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck2'}),
			'wawancara':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck3'}),
			'ots':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck4'}),
			'sp3k':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck5'}),
			'akad':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck6'}),
			'ket_dc':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_slik':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_wawancara':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_ots':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_sp3k':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),
			'ket_akad':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'placeholder':'Keterangan'}),

		}

class TambahKostumerFormPegawai(forms.ModelForm):
	class Meta:
		model = Kostumer
		fields = [
			'nama',
			'kavling',
			'no_ktp',
			'tempat_lahir',
			'tanggal_lahir',
			'alamat',
			'no_hp',
			'pekerjaan',
			'nama_perusahaan',
			'alamat_perusahaan',
			'nama_atasan',
			'no_hp_atasan',
			'nama_pasangan',
			'no_ktp_pasangan',
			'tempat_lahir_pasangan',
			'tanggal_lahir_pasangan',
			'alamat_pasangan',
			'pekerjaan_pasangan',
			'no_hp_pasangan',
			'nama_keluarga',
			'no_ktp_keluarga',
			'alamat_keluarga',
			'no_hp_keluarga',
			'ktp',
			'kartu_keluarga',
			'buku_nikah',
			'npwp',
			'keteranganpenghasilan',
			'foto',
			'rekening_koran',
			'sk_bekerja',
			'sliip_gaji',
			'kartu_pegawai',
			'sku_skhu',
			'neraca',
			'foto_usaha',
			'dc',
			'slik',
			'wawancara',
			'ots',
			'sp3k',
			'akad',]
		def __init__(self):
			pass
		widgets = {
			'kavling':forms.Select(attrs={'class': 'form-control'}),
			'nama':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'tanggal_lahir':forms.TextInput(attrs={'class': 'form-control datepicker','value':'10/20/1970','placeholder':'Pilih Tanggal'}),
			'no_ktp':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'tempat_lahir':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'alamat':forms.Textarea(attrs={'class': 'form-control','placeholder':'Nama'}),
			'pekerjaan':forms.TextInput(attrs={'class': 'form-control','value':'PNS','placeholder':'Nama','disabled':'True'}),
			'no_hp':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),


			'nama_perusahaan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama Perusahaan'}),
			'alamat_perusahaan':forms.Textarea(attrs={'class':'form-control','placeholder':'Alamat Perusahaan '}),
			'nama_atasan':forms.TextInput(attrs={'class':'form-control','placeholder':'Nama Atasan'}),
			'no_hp_atasan':forms.TextInput(attrs={'class':'form-control','placeholder':'No HP Atasan'}),



			'nama_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'tanggal_lahir_pasangan':forms.TextInput(attrs={'class': 'form-control datepicker','value':'10/20/1970','placeholder':'Pilih Tanggal'}),
			'no_ktp_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'tempat_lahir_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'alamat_pasangan':forms.Textarea(attrs={'class': 'form-control','placeholder':'Nama'}),
			'pekerjaan_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_hp_pasangan':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),

			'nama_keluarga':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_ktp_keluarga':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),
			'alamat_keluarga':forms.Textarea(attrs={'class': 'form-control','placeholder':'Nama'}),
			'no_hp_keluarga':forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama'}),

			'ktp':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'kartu_keluarga':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'buku_nikah':forms.FileInput(attrs={'class': 'dropify','name':'dropify' }),
			'npwp':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'keteranganpenghasilan':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'foto':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'rekening_koran':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'sk_bekerja':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'sliip_gaji':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'kartu_pegawai':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'sku_skhu':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'neraca':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'foto_usaha':forms.FileInput(attrs={'class': 'dropify','name':'dropify'}),
			'dc':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck1'}),
			'slik':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck2'}),
			'wawancara':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck3'}),
			'ots':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck4'}),
			'sp3k':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck5'}),
			'akad':forms.CheckboxInput(attrs={'class': 'custom-control-input','id': 'customCheck6'}),


		}


class TambahKavlingForm(forms.ModelForm):
	class Meta:
		model = Kavling
		fields = [
			'nama_kavling',
			'hook',
			'harga_standar',
			'booking',
			'uang_muka',
			'klt',
			'biaya_strategis',
			'plafon',
			]
		def __init__(self):
			pass
		widgets = {
			'nama_kavling':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Kavling'}),
			'hook':forms.TextInput(attrs={'class': 'form-control','placeholder':'Rp. '}),
			'harga_standar':forms.TextInput(attrs={'class': 'form-control','placeholder':'Rp. '}),
			'booking':forms.TextInput(attrs={'class': 'form-control','placeholder':'Rp. '}),
			'uang_muka':forms.TextInput(attrs={'class': 'form-control','placeholder':'Rp. '}),
			'klt':forms.TextInput(attrs={'class': 'form-control','placeholder':'Rp. '}),
			'biaya_strategis':forms.TextInput(attrs={'class': 'form-control','placeholder':'Rp. '}),
			'plafon':forms.TextInput(attrs={'class': 'form-control','placeholder':'Rp. '}),
		}



class TambahMarketerForm(forms.ModelForm):
	"""docstring for TambahMarketerForm"""

	class Meta:
		model = Marketer
		fields = [
			'nama',
			'no_hp',
			'email',

		]
		widgets = {
		'nama':forms.TextInput(attrs={'class':'form-control','placeholder':'Nama Lengkap','style':'padding: 0 30px 0 25px; width: 100%; background: #f4f6fb; height: 50px; border-radius: 22px;'}),
		'no_hp':forms.TextInput(attrs={'class':'form-control','placeholder':'No HP','style':'padding: 0 30px 0 25px; width: 100%; background: #f4f6fb; height: 50px; border-radius: 22px;'}),

		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','style':'padding: 0 30px 0 25px; width: 100%; background: #f4f6fb; height: 50px; border-radius: 22px;'}),

			}





class KegiatanForm(forms.ModelForm):
	"""docstring for TambahMarketerForm"""

	class Meta:
		model = Kegiatan_Marketingnya
		fields = ['marketer',
		'judul_kegiatan',
		'deskripsi',
		]
		widgets = {
		'marketer':forms.TextInput(attrs={'class':'form-control','placeholder': 'Masukan ID Anda'}),
		'judul_kegiatan':forms.TextInput(attrs={'class':'form-control','placeholder':'Judul Kegiatan'}),

		'deskripsi':forms.Textarea(attrs={'class':'form-control','placeholder':'Deskripsi'}),

			}




