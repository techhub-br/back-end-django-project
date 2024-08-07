from django.contrib import admin
from techhub.models import Projects

class AdminProjects(admin.ModelAdmin):
    list_display = ("id", "title", "publish")
    list_display_links = ("id", "title")
    list_filter = ("category", )
    list_editable = ("publish", )
    list_per_page = 10

admin.site.register(Projects, AdminProjects)
