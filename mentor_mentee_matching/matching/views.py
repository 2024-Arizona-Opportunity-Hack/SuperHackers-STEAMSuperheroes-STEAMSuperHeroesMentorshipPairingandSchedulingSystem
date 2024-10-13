from django.shortcuts import render
from .models import Mentor, Mentee, Pair

def match_mentors(mentee):
    mentors = Mentor.objects.filter(location=mentee.location)
    return mentors