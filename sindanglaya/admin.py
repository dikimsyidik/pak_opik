from django.contrib import admin
from .models import Kavling,Kostumer,Marketer,Kegiatan_Marketingnya
# Register your models here.

admin.site.register(Kostumer)
admin.site.register(Kavling)
admin.site.register(Marketer)
admin.site.register(Kegiatan_Marketingnya)
