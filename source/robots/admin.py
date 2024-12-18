from django.contrib import admin
from robots.models import Robot


class RobotAdmin(admin.ModelAdmin):
    list_display = ('serial', 'model', 'version', 'created')
    list_filter = ('serial', 'model', 'version', 'created')


admin.site.register(Robot)
