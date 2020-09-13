from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ngodetail(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	authority = models.CharField(max_length=200, null=True)
	registrationnum = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class donordetail(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class medicine(models.Model):
	medicinename = models.CharField(max_length=200, null=True)
	companyname = models.CharField(max_length=200, null=True)
	manufacturing =models.DateField()
	expiry = models.DateField()
	tablets = models.CharField(max_length=200, null=True)
	

	def __str__(self):
		return self.medicinename




# class post(models.Model):
# 	desc = models.CharField(max_length=200, null=True)
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	timestamp=models.DateTimeField(auto_now_add=True, blank=True)
# 	def __str__(self):
# 		return self.desc[:7]


# class postngo(models.Model):
# 	desc = models.CharField(max_length=200, null=True)
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	timestamp=models.DateTimeField(auto_now_add=True, blank=True)
# 	def __str__(self):
# 		return self.desc[:7]



