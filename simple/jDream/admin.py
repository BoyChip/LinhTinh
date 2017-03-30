from django.contrib import admin
from .models import KhachHang, NhanVien, Hang, HDBan,ChiTietHDBan
# Register your models here.
admin.site.register(KhachHang)
admin.site.register(NhanVien)
admin.site.register(Hang)
admin.site.register(HDBan)
admin.site.register(ChiTietHDBan)