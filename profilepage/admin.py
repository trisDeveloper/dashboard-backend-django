from django.contrib import admin

from profilepage.models import Dashuser, Todolist, Linkslist

# Register your models here.

admin.site.register(Dashuser)
admin.site.register(Todolist)
admin.site.register(Linkslist)