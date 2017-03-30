from django.conf.urls import url
from . import views

urlpatterns = [
# Khách Hàng
	# Tạo khách hàng
	url(r'^KhachHang/Create/$', views.create_khach_hang, name='create_khach_hang'),
	# Hiện thị khách hàng
	url(r'^KhachHang/View/$', views.view_khach_hang, name='view_khach_hang'),
	# Đổi thông tin khách hàng
	url(r'^KhachHang/(?P<pk>[0-9-a-z-A-Z]+)/Change/$', views.change_khach_hang, 
		name='change_khach_hang'
	),
	# Xóa khách hàng
	url(r'^KhachHang/(?P<pk>[0-9-a-z-A-Z]+)/Delete/$', views.delete_khach_hang, 
		name='delete_khach_hang'
	),
	# Hiển thị khách hàng đã chọn
	url(r'^KhachHang/Display/Selected/$', views.display_selected_khach_hang,
		name='display_selected_khach_hang'
	),
	# Xóa khách hàng đã chọn
	url(r'^KhachHang/Delete/Selected/$', views.delete_selected_khach_hang,
		name='delete_selected_khach_hang'
	),
# Hàng hóa
	# Tạo hàng
	url(r'^Hang/Create/$', views.create_hang, name='create_hang'),
	# Hiện thị hàng
	url(r'^Hang/View/$', views.view_hang, name='view_hang'),
	# Cập nhật hàng hóa
	url(r'^Hang/(?P<pk>[0-9-a-z-A-Z]+)/Change/$', views.change_hang,
		name='change_hang'
	),
	# Xóa hàng hóa
	url(r'^Hang/(?P<pk>[0-9-a-z-A-Z]+)/Delete/$', views.delete_hang,
		name='delete_hang'
	),
	# Hiển thị hàng hóa đã chọn
	url(r'^Hang/Display/Selected/$', views.display_selected_hang,
		name='display_selected_hang'
	),
	# Xóa hàng hóa đã chọn
	url(r'^Hang/Delete/Selected/$', views.delete_selected_hang,
		name='delete_selected_hang'
	),
# Nhân viên
	# Hiện thị nhân viên
	url(r'^NhanVien/View/$', views.view_nhan_vien, name='view_nhan_vien'),
	# Tạo nhân Viên
	url(r'^NhanVien/Create/$', views.create_nhan_vien, name='create_nhan_vien'),
	# Cập nhật nhân viên
	url(r'^NhanVien/(?P<pk>[a-zA-Z0-9]+)/Change/$', views.change_nhan_vien,
		name='change_nhan_vien'
	),
	# Cập nhật nhân viên
	url(r'^NhanVien/(?P<pk>[a-zA-Z0-9]+)/Delete/$', views.delete_nhan_vien,
		name='delete_nhan_vien'
	),
	# Hiển thị nhân viên đã chọn
	url(r'^NhanVien/Display/Selected/$', views.display_selected_nhan_vien,
		name='display_selected_nhan_vien'
	),
	# Xóa nhân viên đã chọn
	url(r'^NhanVien/Delete/Selected/$', views.delete_selected_nhan_vien,
		name='delete_selected_nhan_vien'
	),
# Hóa đơn bán
	# Hiện thị hóa đơn bán
	url(r'^HDBan/View/$', views.view_HDBan, name='view_HDBan'),
	# Tạo hóa đơn bán
	url(r'^HDBan/Create/$', views.create_HDBan, name='create_HDBan'),
]