from django.contrib import admin
from robots.models import Robot, RobotProduction


class RobotAdmin(admin.ModelAdmin):
    list_display = ('serial', 'model', 'version', 'created')
    list_filter = ('serial', 'model', 'version', 'created')

class RobotProductionAdmin(admin.ModelAdmin):
    list_display = ('robot', 'quantity', 'produced_at')
    list_filter = ('robot', 'produced_at')

admin.site.register(Robot, RobotAdmin)
admin.site.register(RobotProduction, RobotProductionAdmin)
