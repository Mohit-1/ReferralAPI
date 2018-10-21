from django.db import models
import uuid

# Create your models here.
class Partner(models.Model):
	username = models.CharField(max_length=20, null=True)
	email = models.EmailField(max_length=20, unique=True)
	referral_code = models.CharField(null=True, default=None, editable=False, unique=True, max_length=6)
	referral_credits = models.IntegerField(default=5, editable=False)
	course_credits = models.IntegerField(default=0, editable=False)

	def __str__(self):
		return self.username

	def save(self, *args, **kwargs):
		if self.referral_code is None:
			code = uuid.uuid4().hex.upper()[:6]
			self.referral_code = code
		super(Partner, self).save(*args, **kwargs)

class Referral(models.Model):
	referrer = models.ForeignKey('Partner', to_field='referral_code', on_delete=models.CASCADE)
	referred_email = models.EmailField(max_length=20)	

	def __str__(self):
		return self.referrer.referral_code + "-" + self.referred_email