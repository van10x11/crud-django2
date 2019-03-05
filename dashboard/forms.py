from django import forms
from .models import Mahasiswa


class MahasiswaForm(forms.ModelForm):
	class Meta:
		model = Mahasiswa

		fields = '__all__'

		widgets = {
			'nim':forms.NumberInput(attrs={'placeholder':'Nim'}),
			'nama':forms.TextInput(attrs={'placeholder':'Nama Mahasiswa'}),
			'jenis_kelamin':forms.RadioSelect(),
			'tempat_lahir':forms.TextInput(attrs={'placeholder':'Tempat Lahir'}),
			'tanggal_lahir':forms.DateInput(attrs={'type':'date'}),
			'agama':forms.Select(),
			'email':forms.EmailInput(attrs={'placeholder':'Email'}),
			'alamat':forms.Textarea(attrs={'placeholder':'alamat'}),
			'nama_ibu':forms.TextInput(attrs={'placeholder':'Nama Ibu'}),
		}  