from django.db import models



# model mahasiswa
class Mahasiswa(models.Model):
	nim = models.IntegerField(primary_key=True)
	nama = models.CharField(max_length=50)
	jenis_kelamin = models.CharField(max_length=1,choices=(
		('L','Laki-laki'),
		('P','Perempuan'),
	),default=None)
	tempat_lahir = models.CharField(max_length=50)
	tanggal_lahir = models.DateField()
	agama = models.CharField(max_length=10,choices=(
		('islam','Islam'),
		('kristen','Kristen'),
		('hindu','Hindu'),
		('budha','Budha'),
		('lain','Lain-lain')
	),default=None)
	email = models.EmailField()
	alamat = models.TextField()
	nama_ibu = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.nim}:{self.nama}"
