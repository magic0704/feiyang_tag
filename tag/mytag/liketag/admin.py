from django.contrib import admin

# Register your models here.
#from mytag.liketag.models import user,tag,content
from liketag.models import user,tag,content
admin.site.register(user)
admin.site.register(tag)
admin.site.register(content)
