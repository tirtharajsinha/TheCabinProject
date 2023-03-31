from django.contrib import admin
from .models import Apps, Services, AppOrder, SystemVar
# Register your models here.

admin.site.register(Apps)
admin.site.register(Services)
admin.site.register(AppOrder)
admin.site.register(SystemVar)
