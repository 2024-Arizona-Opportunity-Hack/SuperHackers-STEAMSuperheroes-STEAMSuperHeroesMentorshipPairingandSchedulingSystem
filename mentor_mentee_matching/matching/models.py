from django.db import models

class Mentor(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    session_type = models.CharField(max_length=200)
    ethnicity = models.CharField(max_length=200)
    ethnicity_preference = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    gender_preference = models.CharField(max_length=100)
    mentoring_methods = models.CharField(max_length=200)
    role = models.CharField(max_length=50, choices=[('mentor', 'Mentor'), ('mentee', 'Mentee')])

    def __str__(self):
        return self.name

class Mentee(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    session_type = models.CharField(max_length=200)
    ethnicity = models.CharField(max_length=200)
    ethnicity_preference = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    gender_preference = models.CharField(max_length=100)
    mentoring_methods = models.CharField(max_length=200)
    role = models.CharField(max_length=50, choices=[('mentor', 'Mentor'), ('mentee', 'Mentee')])

    def __str__(self):
        return self.name

class Pair(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    session_details = models.TextField()
    
    def __str__(self):
        return f"{self.mentor.name} - {self.mentee.name}"