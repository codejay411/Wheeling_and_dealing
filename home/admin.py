from django.contrib import admin
from .models import ngodetail, donordetail, medicine

# Register your models here.
admin.site.register(ngodetail)
admin.site.register(donordetail)
admin.site.register(medicine)
# admin.site.register(post)
# admin.site.register(postngo)