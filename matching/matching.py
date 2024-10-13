from geopy.distance import geodesic
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="my_app")

def get_coordinates(city, state):
    location = geolocator.geocode(f"{city}, {state}")
    if location:
        return (location.latitude, location.longitude)
    return None 

def find_distance(city1, state1, city2, state2):
    coords_1 = get_coordinates(city1, state1)
    coords_2 = get_coordinates(city2, state2)

    if coords_1 is None or coords_2 is None:
        return False
    
    return geodesic(coords_1, coords_2).miles <= 60

def match_mentor_to_mentee(mentors, mentees):
    matches = []
    
    for mentee in mentees:
        for mentor in mentors:
            if not is_valid_match(mentor, mentee):
                continue
            
            if age_check(mentor, mentee) and \
               mentoring_type_check(mentor, mentee) and \
               ethnicity_check(mentor, mentee) and \
               gender_check(mentor, mentee):
                matches.append((mentor, mentee))
                print(f"Match found: {mentor.name} with {mentee.name}")
    
    return matches

def is_valid_match(mentor, mentee):
    return find_distance(mentor.city, mentor.state, mentee.city, mentee.state)

# Include other checking functions (age_check, mentoring_type_check, etc.) 

def age_check(mentor, mentee):
    if mentor.age <= mentee.age:
        return False
    if mentor.mentoring_type == 'homework help':
        return (mentor.age - mentee.age) >= 2
    else:
        return (mentor.age - mentee.age) >= 10

def mentoring_type_check(mentor, mentee):
    return mentor.mentoring_type in mentee.mentoring_type

def ethnicity_check(mentor, mentee):

    mentor_ethnicity = mentor.ethnicity  # The mentor's ethnicity from form
    mentee_ethnicity = mentee.ethnicity  # The mentee's ethnicity from form
    mentee_preference = mentee.ethnicity_preference

    if mentee_preference == 'Prefer ONLY to be matched within that similarity':
        return mentor_ethnicity in mentee_ethnicity
    elif mentee_preference == 'Prefer it, but available to others as needed':
        return mentor_ethnicity in mentee_ethnicity
    elif mentee_preference == 'Prefer NOT to be matched within that similarity':
        return mentor_ethnicity not in mentee_ethnicity
    elif mentee_preference == 'Do not have a preference.  Either is fine.':
        return True
    return True

def gender_check(mentor, mentee):
    mentor_gender = mentor.gender  # The mentor's gender from form
    mentee_gender = mentee.gender  # The mentee's gender from form
    mentee_preference = mentee.gender_preference

    if mentee_preference == 'Prefer ONLY to be matched within that similarity':
        return mentor_gender in mentee_gender
    elif mentee_preference == 'Prefer it, but available to others as needed':
        return mentor_gender in mentee_gender 
    elif mentee_preference == 'Prefer NOT to be matched within that similarity':
        return mentor_gender not in mentee_gender
    elif mentee_preference == 'Do not have a preference.  Either is fine.':
        return True
    return True
