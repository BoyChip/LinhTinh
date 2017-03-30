from django.core.exceptions import ValidationError

class MinimumLengthValidator(object):
	def __init__(self, min_length=8):
		self.min_length = min_length

	def validate(self, password, user=None):
		if len(password) < self.min_length:
			raise ValidationError(
				"Mật khẩu ít nhất là %(min_length)d ký tự.",
				code="password_too_short",
				params={'min_length': self.min_length}
			)
	def get_help_text(self):
		return "Mật khẩu ít nhất là %(min_length)d ký tự." % {'min_length': self.min_length}

class NumericPasswordValidator(object):
	def validate(self, password, user=None):
		if password.isdigit():
			raise ValidationError(
				"Mật khẩu toàn là ký tự số.",
				code="password_entirely_numeric"
			)
	def get_help_text(self):
		return "Mật khẩu toàn là ký tự số."