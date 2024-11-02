from django.contrib import admin
from .models import Event, Attendance

# Admin class to display event and attendance count
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue', 'registration_limit', 'attendance_count')

    # Method to calculate attendance count for each event
    def attendance_count(self, obj):
        return obj.attendance_set.count()
    attendance_count.short_description = 'Attendance Count'

# Register models with the admin
admin.site.register(Event, EventAdmin)
admin.site.register(Attendance)
