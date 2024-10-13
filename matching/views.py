from django.shortcuts import render
from .models import Mentor, Mentee, Pair
from .matching import match_mentor_to_mentee

def match_mentors(mentee):
    mentors = Mentor.objects.filter(location=mentee.location)
    return mentors

def match_view(request):
    mentors = Mentor.objects.all()  # Retrieve all mentors
    mentees = Mentee.objects.all()  # Retrieve all mentees
    matches = match_mentor_to_mentee(mentors, mentees)

    print(f"Mentors: {mentors}")
    print(f"Mentees: {mentees}")
    print(f"Matches: {matches}")

    return render(request, 'matching/match_results.html', {'matches': matches})

from rest_framework import viewsets
from .models import Pair
from .serializers import PairSerializer

class PairViewSet(viewsets.ModelViewSet):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer