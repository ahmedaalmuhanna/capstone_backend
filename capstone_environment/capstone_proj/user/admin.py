from django.contrib import admin

# Register your models here.


from .models import Profile
# Register your models here.
myModels = [ Profile]
admin.site.register(myModels)

