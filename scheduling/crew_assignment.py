from pulp import LpMinimize, LpProblem, LpVariable, lpSum
from .models import CrewMember, Flight, Assignment

def assign_crew():
    # Fetch all crew members and flights from the database
    crew_members = list(CrewMember.objects.all())
    flights = list(Flight.objects.all())

    # Create a linear programming problem
    prob = LpProblem("Crew_Scheduling", LpMinimize)

    # Decision variables: X[crew, flight] = 1 if assigned, 0 otherwise
    X = {(c.id, f.id): LpVariable(f"X_{c.id}_{f.id}", 0, 1, cat="Binary") for c in crew_members for f in flights}

    # Objective Function: Minimize the total number of assigned crew (simplified cost)
    prob += lpSum(X[c.id, f.id] for c in crew_members for f in flights)

    # Constraint 1: Each flight must have enough crew members
    required_crew_per_flight = 2  # Example: Each flight needs 2 crew members
    for f in flights:
        prob += lpSum(X[c.id, f.id] for c in crew_members) >= required_crew_per_flight

    # Constraint 2: Crew members cannot exceed their max weekly hours
    for c in crew_members:
        max_hours = c.max_hours_per_week
        prob += lpSum(X[c.id, f.id] * f.duration_hours for f in flights) <= max_hours

    # Solve the LP problem
    prob.solve()

    # Store results in the database
    Assignment.objects.all().delete()  # Clear previous assignments
    for c in crew_members:
        for f in flights:
            if X[c.id, f.id].varValue == 1:
                Assignment.objects.create(crew_member=c, flight=f)
    
    return "Crew assigned successfully!"
