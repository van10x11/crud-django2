from django.shortcuts import render,redirect
from .models import Mahasiswa
from .forms import MahasiswaForm
from django.db.models import Q


# untuk export pdf
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML




# pdf list mahasiswa
def MahasiswaIndexPdf(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		list_mahasiswa = Mahasiswa.objects.all()
		html_string = render_to_string('dashboard/list_mahasiswa.html',{'list_mahasiswa':list_mahasiswa})

		html = HTML(string=html_string)
		html.write_pdf(target='/tmp/list_mahasiswa.pdf')

		fs = FileSystemStorage('/tmp')
		with fs.open('list_mahasiswa.pdf') as pdf:
			response = HttpResponse(pdf,content_type='application/pdf')
			response['Content-Disposition'] = 'attachment; filename="list_mahasiswa.pdf"'
			return response

		return response
	else:
		return redirect('login')

# pdf biodata mahasiswa
def MahasiswaBiodataPdf(request,nim_mahasiswa):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		biodata_mahasiswa = Mahasiswa.objects.get(nim=nim_mahasiswa)
		html_string = render_to_string('dashboard/biodata_mahasiswa_pdf.html',{'biodata_mahasiswa':biodata_mahasiswa})

		html = HTML(string=html_string)
		html.write_pdf(target='/tmp/biodata_mahasiswa.pdf')

		fs = FileSystemStorage('/tmp')
		with fs.open('biodata_mahasiswa.pdf') as pdf:
			response = HttpResponse(pdf,content_type='application/pdf')
			response['Content-Disposition'] = 'attachment; filename="biodata_mahasiswa.pdf"'
			return response
		return response

	else:
		return redirect('login')



def MahasiswaIndex(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		list_mahasiswa = Mahasiswa.objects.all().order_by('nama')
		username = request.user.username
		context = {
			'title':'Daftar Mahasiswa',
			'list_mahasiswa':list_mahasiswa,
			'username':username,
		}
		return render(request,'dashboard/mahasiswa_index.html',context)
	else:
		return redirect('login')


def MahasiswaTambah(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		form_mahasiswa = MahasiswaForm(request.POST or None)
		if request.method == "POST":
			if form_mahasiswa.is_valid():
				form_mahasiswa.save()
				return redirect('dashboard:index')
		context = {
			'title':'Tambah Mahasiswa',
			'form_mahasiswa':form_mahasiswa,
		}
		return render(request,'dashboard/mahasiswa_tambah.html',context)
	else:
		return redirect('login')

def MahasiswaUbah(request,nim_mahasiswa):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		list_mahasiswa = Mahasiswa.objects.get(nim=nim_mahasiswa)
		form_mahasiswa = MahasiswaForm(request.POST or None,instance=list_mahasiswa)
		if request.method == "POST":
			if form_mahasiswa.is_valid():
				form_mahasiswa.save()
				return redirect('dashboard:index')
		context = {
			'title':'Ubah Mahasiswa',
			'form_mahasiswa':form_mahasiswa,
		}
		return render(request,'dashboard/mahasiswa_ubah.html',context)
	else:
		return redirect('login')

def MahasiswaHapus(request,nim_mahasiswa):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		mahasiswa = Mahasiswa.objects.get(nim=nim_mahasiswa)
		mahasiswa.delete()
		return redirect('dashboard:index')
	else:
		return redirect('login')

def MahasiswaBiodata(request,nim_mahasiswa):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		mahasiswa = Mahasiswa.objects.get(nim=nim_mahasiswa)
		context = {
			'title':'Biodata Mahasiswa',
			'mahasiswa':mahasiswa,
		}
		return render(request,'dashboard/mahasiswa_biodata.html',context)
	else:
		return redirect('login')

def MahasiswaCari(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		username = request.user.username
		cari = request.GET['cari']
		list_mahasiswa = Mahasiswa.objects.filter(Q(nama__contains=cari)|Q(nim__contains=cari)|Q(jenis_kelamin__contains=cari)|Q(alamat__contains=cari))
		banyak_data = list_mahasiswa.count()
		if banyak_data != 0:
			banyak_data = banyak_data
		else:
			banyak_data = 'tidak ada data'
		context = {
			'title':'Daftar Mahasiswa',
			'list_mahasiswa':list_mahasiswa,
			'banyak_data':banyak_data,
			'username':username,
		}
		return render(request,'dashboard/mahasiswa_index.html',context)
	else:
		return redirect('login')
