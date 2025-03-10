from rest_framework import serializers
from .models import CrewMember, Flight, Assignment

class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    crew_member = CrewMemberSerializer()
    flight = FlightSerializer()

    class Meta:
        model = Assignment
        fields = '__all__'
