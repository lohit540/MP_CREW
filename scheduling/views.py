from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Assignment
from .serializers import AssignmentSerializer
from .crew_assignment import assign_crew
from django.shortcuts import render
from .models import Assignment

@api_view(['GET'])
def get_assignments(request):
    assignments = Assignment.objects.all()
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def run_crew_assignment(request):
    assign_crew()
    return Response({"message": "Crew assignment completed!"})


def assignment_list(request):
    return render(request, 'scheduling/assignments.html')
def home(request):
   assignments = Assignment.objects.all()
   return render(request, 'home.html', {'assignments': assignments})
 