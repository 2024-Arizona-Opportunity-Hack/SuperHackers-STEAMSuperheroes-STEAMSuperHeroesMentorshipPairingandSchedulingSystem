from django.contrib import admin
from .models import Mentor, Mentee, Pair

admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Pair)