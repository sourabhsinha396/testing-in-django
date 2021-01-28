from django.contrib import admin

from .models import Role, Location, Job


class RoleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Role, RoleAdmin)


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Location, LocationAdmin)


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "publish"]
    search_fields = ["title", "job_description"]


admin.site.register(Job, JobAdmin)
