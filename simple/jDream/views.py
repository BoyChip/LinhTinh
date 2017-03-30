from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import (
	KhachHangCreateForm, KhachHangChangeForm, KhachHangDeleteForm,
	HangCreateForm, HangChangeForm, HangDeleteForm,
	NhanVienCreateForm, NhanVienChangeForm, NhanVienDeleteForm,
	HDBanCreateForm,
)
from .models import KhachHang, Hang, NhanVien, HDBan
# Create your views here.
# Khách Hàng
#Hiện thị Khách Hàng
def view_khach_hang(request):
	return render(request, 'KhachHang/ViewKhachHang.html', {'form': KhachHang.objects.all()})
# Tạo khách hàng
def create_khach_hang(request):
	if request.method == 'POST':
		form = KhachHangCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('jDream:view_khach_hang'))
	else:
		form = KhachHangCreateForm()
	return render(request, 'KhachHang/KhachHangCreateForm.html', {'form': form})

# Đổi thông tin khách hàng
def change_khach_hang(request, pk):
	instance = get_object_or_404(KhachHang, pk=pk)
	if request.method == 'POST':
		form = KhachHangChangeForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return redirect(reverse('jDream:view_khach_hang'))
	else:
		form = KhachHangChangeForm(instance=instance)
	return render(request, 'KhachHang/KhachHangChangeForm.html', {'form':form, 'pk': pk})
# Xóa khách hàng
def delete_khach_hang(request, pk):
	instance = get_object_or_404(KhachHang, pk=pk)
	if request.method == 'POST':
		instance.delete()
		return redirect(reverse('jDream:view_khach_hang'))
	else:
		form = KhachHangDeleteForm(instance=instance)
	return render(request, 'KhachHang/KhachHangDeleteForm.html', {'form': form})
# Hiển thị khách hàng đã chọn
def display_selected_khach_hang(request):
	instances = KhachHang.objects.filter(pk__in=request.POST.getlist('Items'))
	return render(request, 'KhachHang/KhachHangDeleteSelectForm.html', {'instances': instances})
# Xóa khách hàng đã chọn
def delete_selected_khach_hang(request):
	if request.method == 'POST':
		KhachHang.objects.filter(pk__in=request.POST.getlist('pk')).delete()		
		return redirect(reverse('jDream:view_khach_hang'))
# Hàng hóa
# Hiện thị hàng hóa
def view_hang(request):
	return render(request, 'Hang/ViewHang.html', {'form': Hang.objects.all()})
# Tạo hàng hóa
def create_hang(request):
	if request.method == 'POST':
		form = HangCreateForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect(reverse('jDream:view_hang'))
	else:
		form = HangCreateForm()
	return render(request, 'Hang/HangCreateForm.html', {'form': form})
# Cập nhật hàng hóa
def change_hang(request, pk):
	instance = get_object_or_404(Hang, pk=pk)
	if request.method == 'POST':
		form = HangChangeForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			return redirect(reverse('jDream:view_hang'))
	else:
		form = HangChangeForm(instance=instance)
	return render(request, 'Hang/HangChangeForm.html', {'form': form, 'pk': pk})
# Xóa hàng hóa
def delete_hang(request, pk):
	instance = get_object_or_404(Hang, pk=pk)

	if request.method == 'POST':
		instance.delete()
		return redirect(reverse('jDream:view_hang'))
	else:
		form = HangDeleteForm(instance=instance)
	return render(request, 'Hang/HangDeleteForm.html', {'form': form})
# Hiện thị hàng hóa đã chọn
def display_selected_hang(request):
	instances = Hang.objects.filter(pk__in=request.POST.getlist('Items'))
	return render(request, 'Hang/HangDeleteSelectedForm.html', {'instances': instances})
# Xóa hàng hóa đã chọn
def delete_selected_hang(request):
	if request.method == 'POST':
		Hang.objects.filter(pk__in=request.POST.getlist('pk')).delete()
		return redirect(reverse('jDream:view_hang'))
# Nhân viên
# Hiện thị nhân viên
def view_nhan_vien(request):
	return render(request, 'NhanVien/ViewNhanVien.html', {'form': NhanVien.objects.all()})
# Tạo nhân viên
def create_nhan_vien(request):
	if request.method == 'POST':
		form = NhanVienCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('jDream:view_nhan_vien'))
	else:
		form = NhanVienCreateForm()
	return render(request, 'NhanVien/NhanVienCreateForm.html', {'form': form})
# Cập nhật nhân viên
def change_nhan_vien(request, pk):
	instance = get_object_or_404(NhanVien, pk=pk)
	if request.method == 'POST':
		form = NhanVienChangeForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return redirect(reverse('jDream:view_nhan_vien'))
	else: form = NhanVienChangeForm(instance=instance)
	return render(request, 'NhanVien/NhanVienChangeForm.html', {'form': form, 'pk': pk})
# Xóa nhân viên
def delete_nhan_vien(request, pk):
	instance = get_object_or_404(NhanVien, pk=pk)

	if request.method == 'POST':
		instance.delete()
		return redirect(reverse('jDream:view_hang'))
	else:
		form = NhanVienDeleteForm(instance=instance)
	return render(request, 'NhanVien/NhanVienDeleteForm.html', {'form': form})
# Hiện thị nhân viên đã chọn
def display_selected_nhan_vien(request):
	instances = NhanVien.objects.filter(pk__in=request.POST.getlist('Items'))
	return render(request, 'NhanVien/NhanVienDeleteSelectedForm.html', {'instances': instances})
# Xóa nhân viên đã chọn
def delete_selected_nhan_vien(request):
	if request.method == 'POST':
		NhanVien.objects.filter(pk__in=request.POST.getlist('pk')).delete()
		return redirect(reverse('jDream:view_nhan_vien'))
# Hóa đơn bán
# Hiện thị hóa đơn bán
def view_HDBan(request):
	return render(request, 'HDBan/ViewHDBan.html', {'form': HDBan.objects.all()})
# Tạo hóa đơn bán
def create_HDBan(request):
	if request.method == 'POST':
		form = HDBanCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('jDream:view_HDBan'))
	else:
		form = HDBanCreateForm()
	return render(request, 'HDBan/HDBanCreateForm.html', {'form':form})