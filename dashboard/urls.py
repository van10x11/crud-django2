from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
	path('',views.MahasiswaIndex,name='index'),
	path('tambah-mahasiswa/',views.MahasiswaTambah,name='mahasiswa-tambah'),
	path('ubah-mahasiswa/<int:nim_mahasiswa>',views.MahasiswaUbah,name='mahasiswa-ubah'),
	path('hapus-mahasiswa/<int:nim_mahasiswa>',views.MahasiswaHapus,name='mahasiswa-hapus'),
	path('biodata-mahasiswa/<int:nim_mahasiswa>',views.MahasiswaBiodata,name='mahasiswa-biodata'),
	path('cari/mahasiswa/result',views.MahasiswaCari,name='mahasiswa-cari'),

	# pdf daftar mahasiswa
	path('list-mahasiswa/pdf/',views.MahasiswaIndexPdf,name='mahasiswa-pdf'),

	# pdf biodata mahasiswa
	path('biodata-mahasiswa/pdf/<int:nim_mahasiswa>',views.MahasiswaBiodataPdf,name='mahasiswa-biodata-pdf'),
]