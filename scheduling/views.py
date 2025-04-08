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
from pulp import LpProblem, LpMinimize, LpVariable, lpSum

def crew_scheduler():
    flights = ['F1', 'F2', 'F3']
    crews = ['C1', 'C2']

    # Cost of assigning crew to flights (lower is better)
    cost = {
        ('C1', 'F1'): 500, ('C1', 'F2'): 600, ('C1', 'F3'): 200,
        ('C2', 'F1'): 300, ('C2', 'F2'): 400, ('C2', 'F3'): 700,
    }

    # Create binary decision variables
    x = LpVariable.dicts("assign", (crews, flights), cat='Binary')

    # LP Problem
    model = LpProblem("Crew_Scheduling", LpMinimize)

    # Objective: Minimize total assignment cost
    model += lpSum(cost[c, f] * x[c][f] for c in crews for f in flights)

    # Constraint: Each flight gets exactly one crew
    for f in flights:
        model += lpSum(x[c][f] for c in crews) == 1

    # Optional constraint: each crew does at most 2 flights
    for c in crews:
        model += lpSum(x[c][f] for f in flights) <= 2

    # Solve
    model.solve()

    # Get results
    assignment = []
    for c in crews:
        for f in flights:
            if x[c][f].value() == 1:
                assignment.append((c, f))

    return assignment


def view_assignments(request):
    assignments = crew_scheduler()
    return render(request, 'assignments.html', {'assignments': assignments})
