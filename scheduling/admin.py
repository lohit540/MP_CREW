from django.contrib import admin
from .models import CrewMember, Flight, Assignment

@admin.register(CrewMember)
class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'max_hours_per_week')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'origin', 'destination', 'departure_time', 'duration_hours')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('crew_member', 'flight')

