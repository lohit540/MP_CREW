from django.urls import path
from .views import home, assignment_list, get_assignments, run_crew_assignment

urlpatterns = [
    path('', home, name='home'),
    path('assignments-page/', assignment_list, name='assignment_list'),
    path('api/assignments/', get_assignments, name='get_assignments'),
    path('api/assign-crew/', run_crew_assignment, name='run_crew_assignment'),
]
