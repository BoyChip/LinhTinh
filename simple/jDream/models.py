from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
# Khách hàng
class KhachHang(models.Model):
	MaKhachHang = models.CharField(primary_key=True, max_length=10)
	TenKhachHang = models.CharField(max_length=50)
	DiaChi = models.CharField(max_length=100)
	DienThoai = models.CharField(max_length=15)
	def __str__(self):
		return str(self.MaKhachHang)
# Hàng
def directory_path(instance, filename):
	return 'hang_{0}/{1}'.format(instance.pk, filename)

class Hang(models.Model):
	MaHang = models.CharField(primary_key=True, max_length=10)
	TenHang = models.CharField(unique=True, max_length=50)
	SoLuong = models.IntegerField()
	GiaMuaVao = models.DecimalField(max_digits=15, decimal_places=2)
	GiaBanRa = models.DecimalField(max_digits=15, decimal_places=2)
	image = models.ImageField(upload_to=directory_path,blank=True)
	def __str__(self):
		return str(self.MaHang)
# Nhân viên
class NhanVien(models.Model):
	MaNhanVien = models.CharField(primary_key=True, max_length=10)
	TenNhanVien = models.CharField(max_length=50)
	DiaChi = models.CharField(max_length=100)
	DienThoai = models.CharField(max_length=15)
	def __str__(self):
		return str(self.MaNhanVien)
# Hóa đơn bán
class HDBan(models.Model):
	MaHDBan = models.CharField(primary_key=True, max_length=10)
	MaNhanVien = models.ForeignKey('NhanVien', on_delete=models.CASCADE)
	MaKhachHang = models.ForeignKey('KhachHang', on_delete=models.CASCADE)
	NgayBan = models.DateTimeField(auto_now_add=True, blank=True)
	#TongTien = models.DecimalField(max_digits=15, decimal_places=2)
	def __str__(self):
		return str(self.MaHDBan)

# Hóa đơn chi tiết
class ChiTietHDBan(models.Model):
	MaHDBan = models.CharField(primary_key=True, max_length=10)
	MaHang = models.CharField(primary_key=True, max_length=10)
	SoLuong = models.IntegerField()
	ThanhTien = models.DecimalField(max_digits=15, decimal_places=2, default=0)
	MaHDBan = models.ForeignKey('HDBan', on_delete=models.CASCADE)
	MaHang = models.ForeignKey('Hang', on_delete=models.CASCADE)
	def __str__(self):
		return str(self.MaHDBan) + ' ' + str(self.MaHang)

