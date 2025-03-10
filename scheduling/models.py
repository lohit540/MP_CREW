from django.db import models

class CrewMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)  # Pilot, Co-Pilot, Attendant
    max_hours_per_week = models.IntegerField()
    
    def __str__(self):
        return self.name

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    duration_hours = models.FloatField()

    def __str__(self):
        return self.flight_number

class Assignment(models.Model):
    crew_member = models.ForeignKey(CrewMember, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.crew_member} -> {self.flight}"
