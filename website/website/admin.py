from django.contrib import admin
from django.contrib.auth.models import User, Group
from website.models import Project, Image

class ImageInline(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Project, ProjectAdmin)
