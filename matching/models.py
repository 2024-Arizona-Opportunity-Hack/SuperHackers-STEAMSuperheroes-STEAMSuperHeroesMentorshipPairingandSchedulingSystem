from django.db import models
AGE_CHOICES = [
    ('9-13', '9-13'),
    ('13-18', '13-18'),
    ('18-22', '18-22'),
    ('22-30', '22-30'),
    ('30-40', '30-40'),
    ('40-50', '40-50'),
    ('50-60', '50-60'),
    ('60+', '60+'),
]
STATE_CHOICES = [
    ('AL', 'AL: Alabama'),
    ('AK', 'AK: Alaska'),
    ('AZ', 'AZ: Arizona'),
    ('AR', 'AR: Arkansas'),
    ('CA', 'CA: California'),
    ('CO', 'CO: Colorado'),
    ('CT', 'CT: Connecticut'),
    ('DC', 'DC: District of Columbia'),
    ('DE', 'DE: Delaware'),
    ('FL', 'FL: Florida'),
    ('GA', 'GA: Georgia'),
    ('HI', 'HI: Hawaii'),
    ('ID', 'ID: Idaho'),
    ('IL', 'IL: Illinois'),
    ('IN', 'IN: Indiana'),
    ('IA', 'IA: Iowa'),
    ('KS', 'KS: Kansas'),
    ('KY', 'KY: Kentucky'),
    ('LA', 'LA: Louisiana'),
    ('ME', 'ME: Maine'),
    ('MD', 'MD: Maryland'),
    ('MA', 'MA: Massachussetts'),
    ('MI', 'MI: Michigan'),
    ('MN', 'MN: Minnesota'),
    ('MS', 'MS: Mississippi'),
    ('MO', 'MO: Missouri'),
    ('MT', 'MT: Montana'),
    ('NE', 'NE: Nebraska'),
    ('NV', 'NV: Nevada'),
    ('NH', 'NH: New Hampshire'),
    ('NJ', 'NJ: New Jersey'),
    ('NM', 'NM: New Mexico'),
    ('NY', 'NY: New York'),
    ('NC', 'NC: North Carolina'),
    ('ND', 'ND: North Dakota'),
    ('OH', 'OH: Ohio'),
    ('OK', 'OK: Oklahoma'),
    ('OR', 'OR: Oregon'),
    ('PA', 'PA: Pennsylvania'),
    ('RI', 'RI: Rhode Island'),
    ('SC', 'SC: South Carolina'),
    ('SD', 'SD: South Dakota'),
    ('TN', 'TN: Tennessee'),
    ('TX', 'TX: Texas'),
    ('UT', 'UT: Utah'),
    ('VT', 'VT: Vermont'),
    ('VA', 'VA: Virginia'),
    ('WA', 'WA: Washington'),
    ('WV', 'WV: West Virginia'),
    ('WI', 'WI: Wisconsin'),
    ('WY', 'WY: Wyoming'),
]

class Mentor(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    age = models.IntegerField(choices=AGE_CHOICES)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    session_type = models.CharField(max_length=200, choices=[
        ('Homework Help', 'Homework Help'),
        ('Exposure to STEAM', 'Exposure to STEAM'),
        ('College guidance', 'College guidance'),
        ('Career guidance', 'Career guidance'),
        ('Explore a particular field', 'Explore a particular field'),
        ('Other', 'Other'),  # Include 'Other')
    ])
    session_type_others = models.CharField(max_length=100, blank=True, null=True)

    ethnicity = models.CharField(max_length=200, choices=[
        ('American Indian or Alaska Native', 'American Indian or Alaska Native'),
        ('Asian', 'Asian: Includes Chinese, Japanese, Filipino, Korean, South Asian, and Vietnamese'),
        ('South Asian', 'South Asian: Includes Indian, Pakistan, Sri Lankan, Bangladesh'),
        ('Black or African American', 'Black or African American: Includes Jamaican, Nigerian, Haitian, and Ethiopian'),
        ('Hispanic or Latino', 'Hispanic or Latino: Includes Puerto Rican, Mexican, Cuban, Salvadoran, and Colombian'),
        ('Middle Eastern or North African', 'Middle Eastern or North African: Includes Lebanese, Iranian, Egyptian, Moroccan, Israeli, and Palestinian'),
        ('Native Hawaiian or Pacific Islander', 'Native Hawaiian or Pacific Islander: Includes Samoan, Guamanian, Chamorro, and Tongan'),
        ('White or European', 'White or European: Includes German, Irish, English, Italian, Polish, and French'),
        ('Other', 'Other'),  # Include 'Other'
    ])

    ethnicity_other = models.CharField(max_length=100, blank=True, null=True)

    ethnicity_preference = models.CharField(max_length=200, choices=[
        ('Prefer ONLY to be matched within that similarity', 'Prefer ONLY to be matched within that similarity'),
        ('Prefer it, but available to others as needed', 'Prefer it, but available to others as needed'),
        ('Prefer NOT to be matched within that similarity', 'Prefer NOT to be matched within that similarity'),
        ('Do not have a preference. Either is fine.', 'Do not have a preference. Either is fine.'),
        ('Other', 'Other'),  # Include 'Other')
    ])
    
    ethnicity_preference_other = models.CharField(max_length=100, blank=True, null=True)

    gender = models.CharField(max_length=100, choices=[
        ('Cisgender Male', 'Cisgender Male'),
        ('Cisgender Female', 'Cisgender Female'),
        ('Transgender Male', 'Transgender Male'),
        ('Transgender Female', 'Transgender Female'),
        ('Prefer not to disclose', 'Prefer not to disclose'),
        ('Other', 'Other'),  # Include 'Other'
    ])

    gender_other = models.CharField(max_length=100, blank=True, null=True)

    gender_preference = models.CharField(max_length=100, choices=[
        ('Prefer ONLY to be matched within that similarity', 'Prefer ONLY to be matched within that similarity'),
        ('Prefer it, but available to others as needed', 'Prefer it, but available to others as needed'),
        ('Prefer NOT to be matched within that similarity', 'Prefer NOT to be matched within that similarity'),
        ('Do not have a preference. Either is fine.', 'Do not have a preference. Either is fine.'),
        ('Other', 'Other'),
    ])

    gender_preference_other = models.CharField(max_length=100, blank=True, null=True)

    mentoring_methods = models.CharField(max_length=200, choices=[
        ('Web conference', 'Web conference'),
        ('In person', 'In person'),
        ('Hybrid', 'Hybrid (both web and in person)'),
        ('Other', 'Other'),
    ])

    mentoring_methods_other = models.CharField(max_length=100, blank=True, null=True)

    role = models.CharField(max_length=20, choices=[
    ('Mentor', 'Mentor'),
    ('Mentee', 'Mentee'),
    ])

    def __str__(self):
        return self.name
    
class Mentee(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    age = models.IntegerField(choices=AGE_CHOICES)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    session_type = models.CharField(max_length=200, choices=[
        ('Homework Help', 'Homework Help'),
        ('Exposure to STEAM', 'Exposure to STEAM'),
        ('College guidance', 'College guidance'),
        ('Career guidance', 'Career guidance'),
        ('Explore a particular field', 'Explore a particular field'),
        ('Other', 'Other'),  # Include 'Other')
    ])
    session_type_others = models.CharField(max_length=100, blank=True, null=True)

    ethnicity = models.CharField(max_length=200, choices=[
        ('American Indian or Alaska Native', 'American Indian or Alaska Native'),
        ('Asian', 'Asian: Includes Chinese, Japanese, Filipino, Korean, South Asian, and Vietnamese'),
        ('South Asian', 'South Asian: Includes Indian, Pakistan, Sri Lankan, Bangladesh'),
        ('Black or African American', 'Black or African American: Includes Jamaican, Nigerian, Haitian, and Ethiopian'),
        ('Hispanic or Latino', 'Hispanic or Latino: Includes Puerto Rican, Mexican, Cuban, Salvadoran, and Colombian'),
        ('Middle Eastern or North African', 'Middle Eastern or North African: Includes Lebanese, Iranian, Egyptian, Moroccan, Israeli, and Palestinian'),
        ('Native Hawaiian or Pacific Islander', 'Native Hawaiian or Pacific Islander: Includes Samoan, Guamanian, Chamorro, and Tongan'),
        ('White or European', 'White or European: Includes German, Irish, English, Italian, Polish, and French'),
        ('Other', 'Other'),  # Include 'Other'
    ])

    ethnicity_other = models.CharField(max_length=100, blank=True, null=True)

    ethnicity_preference = models.CharField(max_length=200, choices=[
        ('Prefer ONLY to be matched within that similarity', 'Prefer ONLY to be matched within that similarity'),
        ('Prefer it, but available to others as needed', 'Prefer it, but available to others as needed'),
        ('Prefer NOT to be matched within that similarity', 'Prefer NOT to be matched within that similarity'),
        ('Do not have a preference. Either is fine.', 'Do not have a preference. Either is fine.'),
        ('Other', 'Other'),  # Include 'Other')
    ])
    
    ethnicity_preference_other = models.CharField(max_length=100, blank=True, null=True)

    gender = models.CharField(max_length=100, choices=[
        ('Cisgender Male', 'Cisgender Male'),
        ('Cisgender Female', 'Cisgender Female'),
        ('Transgender Male', 'Transgender Male'),
        ('Transgender Female', 'Transgender Female'),
        ('Prefer not to disclose', 'Prefer not to disclose'),
        ('Other', 'Other'),  # Include 'Other'
    ])

    gender_other = models.CharField(max_length=100, blank=True, null=True)

    gender_preference = models.CharField(max_length=100, choices=[
        ('Prefer ONLY to be matched within that similarity', 'Prefer ONLY to be matched within that similarity'),
        ('Prefer it, but available to others as needed', 'Prefer it, but available to others as needed'),
        ('Prefer NOT to be matched within that similarity', 'Prefer NOT to be matched within that similarity'),
        ('Do not have a preference. Either is fine.', 'Do not have a preference. Either is fine.'),
        ('Other', 'Other'),
    ])

    gender_preference_other = models.CharField(max_length=100, blank=True, null=True)

    mentoring_methods = models.CharField(max_length=200, choices=[
        ('Web conference', 'Web conference'),
        ('In person', 'In person'),
        ('Hybrid', 'Hybrid (both web and in person)'),
        ('Other', 'Other'),
    ])

    mentoring_methods_other = models.CharField(max_length=100, blank=True, null=True)

    role = models.CharField(max_length=20, choices=[
    ('Mentor', 'Mentor'),
    ('Mentee', 'Mentee'),
    ])

    def __str__(self):
        return self.name

class Pair(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    session_details = models.TextField()
    
    def __str__(self):
        return f"{self.mentor.name} - {self.mentee.name}"