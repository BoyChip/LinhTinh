from django import forms
from .models import KhachHang, Hang, NhanVien, HDBan

#Tạo khách hàng
class KhachHangCreateForm(forms.ModelForm):
	MaKhachHang = forms.CharField(label='Mã Khách Hàng',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập mã khách hàng'}))
	TenKhachHang = forms.CharField(label='Tên Khách Hàng',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập tên khách hàng'}))
	DiaChi = forms.CharField(label='Địa Chỉ',
		widget=forms.Textarea(attrs={'placeholder': 'Nhập địa chỉ khách hàng'}))
	DienThoai = forms.CharField(label='Điện Thoại',
		widget=forms.NumberInput(attrs={'placeholder': 'Nhập điện thoại'}))

	def clean_MaKhachHang(self):
		MaKhachHang = self.cleaned_data['MaKhachHang']
		if KhachHang.objects.filter(MaKhachHang=MaKhachHang).exists():
			raise forms.ValidationError(
				'Mã khách hàng đã tồn tại',
				code='Ma_Ton_Tai'
			)
		return MaKhachHang
	class Meta:
		model = KhachHang
		fields = '__all__'
# Cập nhật khách hàng
class KhachHangChangeForm(forms.ModelForm):
	TenKhachHang = forms.CharField(label='Tên Khách Hàng',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập tên khách hàng'}))
	DiaChi = forms.CharField(label='Địa Chỉ',
		widget=forms.Textarea(attrs={'placeholder': 'Nhập địa chỉ khách hàng'}))
	DienThoai = forms.CharField(label='Điện Thoại',
		widget=forms.NumberInput(attrs={'placeholder': 'Nhập điện thoại'}))

	def save(self, commit=True):
		khachhang = super(KhachHangChangeForm, self).save(commit=False)
		khachhang.TenKhachHang = self.cleaned_data['TenKhachHang']
		khachhang.DiaChi = self.cleaned_data['DiaChi']
		khachhang.DienThoai = self.cleaned_data['DienThoai']

		if commit:
			khachhang.save()
			return khachhang
	class Meta:
		model = KhachHang
		fields = [
			'TenKhachHang',
			'DiaChi',
			'DienThoai'
		]
# Xóa khách hàng
class KhachHangDeleteForm(KhachHangChangeForm):

	class Meta:
		model = KhachHang
		fields = '__all__'

# Hàng hóa
# Tạo hàng hóa
class HangCreateForm(forms.ModelForm):
	MaHang = forms.CharField(label='Mã Hàng',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập mã hàng'})
	)
	TenHang = forms.CharField(label='Tên Hàng',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập tên hàng'})
	)
	SoLuong = forms.IntegerField(label='Số Lượng',
		widget=forms.NumberInput(attrs={'placeholder': 'Nhập số lượng'})
	)
	GiaMuaVao = forms.DecimalField(label='Giá Mua Vào',
		widget=forms.NumberInput(attrs={'placeholder': 'Nhập giá mua vào'})
	)
	GiaBanRa = forms.DecimalField(label='Giá Bán Ra',
		widget=forms.NumberInput(attrs={'placeholder': 'Nhập giá bán ra'})
	)
	image = forms.ImageField(label='Hình Ảnh')

	def clean_MaHang(self):
		MaHang = self.cleaned_data['MaHang']
		if Hang.objects.filter(MaHang=MaHang).exists():
			raise forms.ValidationError(
				'Mã hàng đã tồn tại',
				code='Ma_Ton_Tai'
			)
		return MaHang
	"""def save(self, commit=True):
		hang = super(HangCreateForm, self).save(commit=False)
		hang.MaHang = self.cleaned_data['MaHang']
		hang.TenHang = self.cleaned_data['TenHang']
		hang.SoLuong = self.cleaned_data['SoLuong']
		hang.GiaMuaVao = self.cleaned_data['GiaMuaVao']
		hang.GiaBanRa = self.cleaned_data['GiaBanRa']
		hang.image = self.cleaned_data['image']

		if commit:
			hang.save();
			return hang"""
	class Meta:
		model = Hang
		fields = '__all__'
# Cập nhật hàng hóa
class HangChangeForm(forms.ModelForm):
	TenHang = forms.CharField(label='Tên Hàng',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập tên hàng'})
	)
	SoLuong = forms.IntegerField(label='Số Lượng',
		widget=forms.NumberInput(attrs={'placeholder': 'Nhập số lượng'})
	)
	GiaMuaVao = forms.DecimalField(label='Giá Mua Vào',
		widget=forms.NumberInput(attrs={'placeholder': 'Nhập giá mua vào'})
	)
	GiaBanRa = forms.DecimalField(label='Giá Bán Ra',
		widget=forms.NumberInput(attrs={'placeholder': 'Nhập giá bán ra'})
	)
	image = forms.ImageField(label='Hình Ảnh')

	def save(self, commit=True):
		hang = super(HangChangeForm, self).save(commit=False)
		hang.TenHang = self.cleaned_data['TenHang']
		hang.SoLuong = self.cleaned_data['SoLuong']
		hang.GiaMuaVao = self.cleaned_data['GiaMuaVao']
		hang.GiaBanRa = self.cleaned_data['GiaBanRa']
		hang.image = self.cleaned_data['image']
		if commit:
			hang.save()
			return hang
	class Meta:
		model = Hang
		fields = [		
			'TenHang',
			'SoLuong',
			'GiaMuaVao',
			'GiaBanRa',
			'image'
		]
# Xóa hàng hóa
class HangDeleteForm(HangChangeForm):
	class Meta:
		model = Hang
		fields = '__all__'
# Nhân viên
class NhanVienCreateForm(forms.ModelForm):
	MaNhanVien = forms.CharField(label='Mã Nhân Viên',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập mã nhân viên'})
	)
	TenNhanVien = forms.CharField(label='Tên Nhân Viên',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập tên nhân viên'})
	)
	DiaChi = forms.CharField(label='Địa Chỉ',
		widget=forms.Textarea(attrs={'placeholder': 'Nhập địa chỉ'})
	)
	DienThoai = forms.CharField(label='Điện Thoại',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập điện thoại'})
	)

	def clean_MaNhanVien(self):
		MaNhanVien = self.cleaned_data['MaNhanVien']
		if NhanVien.objects.filter(MaNhanVien=MaNhanVien).exists():
			raise forms.ValidationError(
				'Mã nhân viên đã tồn tại',
				code='Ma_Ton_Tai'
			)
		return MaNhanVien

	class Meta:
		model = NhanVien
		fields = '__all__'
# Cập nhật nhân viên
class NhanVienChangeForm(forms.ModelForm):
	TenNhanVien = forms.CharField(label='Tên Nhân Viên',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập tên nhân viên'})
	)
	DiaChi = forms.CharField(label='Địa Chỉ',
		widget=forms.Textarea(attrs={'placeholder': 'Nhập địa chỉ'})
	)
	DienThoai = forms.CharField(label='Điện Thoại',
		widget=forms.TextInput(attrs={'placeholder': 'Nhập điện thoại'})
	)

	def save(self, commit=True):
		nhanvien = super(NhanVienChangeForm, self).save(commit=False)
		nhanvien.TenNhanVien = self.cleaned_data['TenNhanVien']
		nhanvien.DiaChi = self.cleaned_data['DiaChi']
		nhanvien.DienThoai = self.cleaned_data['DienThoai']

		if commit:
			nhanvien.save()
			return nhanvien
	class Meta:
		model = NhanVien
		fields = [
			'TenNhanVien',
			'DiaChi',
			'DienThoai'
		]
# Xóa nhân viên
class NhanVienDeleteForm(NhanVienChangeForm):
	class Meta:
		model = NhanVien
		fields = '__all__'
# Hóa đơn bán
# Tạo hóa đơn bán
class HDBanCreateForm(forms.ModelForm):
	MaHDBan = forms.CharField(label="Mã Hóa Đơn",
		widget=forms.TextInput(attrs={'placeholder': 'Nhập mã hóa đơn'})
	)
	MaNhanVien = forms.ModelChoiceField(label="Mã Nhân Viên",
		queryset = NhanVien.objects.all()
	)
	MaKhachHang = forms.ModelChoiceField(label="Mã Khách Hàng",
		queryset = KhachHang.objects.all()
	)

	"""def save(self, commit=True):
		hdban = super(HDBanCreateForm, self).save(commit=False)
		hdban.MaHDBan = self.cleaned_data['MaHDBan']
		hdban.MaNhanVien = self.cleaned_data['MaNhanVien']
		hdban.MaKhachHang = self.cleaned_data['MaKhachHang']

		if commit:
			hdban.save()
			return hdban"""
	class Meta:
		model = HDBan
		fields = [
			'MaHDBan',
			'MaNhanVien',
			'MaKhachHang'
		]