
from django.contrib import admin
from .models import Report,IOCS



class ReportAdmin(admin.ModelAdmin):
    list_display =['title','details','time']  
myModels = [IOCS]
admin.site.register(Report, ReportAdmin)
admin.site.register(myModels)
