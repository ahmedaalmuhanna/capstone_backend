
from django.contrib import admin

from .models import Report,IOCS
# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    list_display =['title','details','time']  
    
myModels = [IOCS]
admin.site.register(Report, ReportAdmin)
admin.site.register(myModels)

# Register your models here.
