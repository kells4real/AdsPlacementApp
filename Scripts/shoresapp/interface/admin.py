from django.contrib import admin
from . models import Ads

class AdsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Ads, AdsAdmin)
