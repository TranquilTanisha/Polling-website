from django.contrib import admin
from .models import ADivCandidate, BDivCandidate, ADivRegistration, BDivRegistration

admin.site.register(ADivCandidate)
admin.site.register(BDivCandidate)
admin.site.register(ADivRegistration)
admin.site.register(BDivRegistration)