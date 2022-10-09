from django.contrib import admin
from .models import ADivPoll, BDivPoll, ADivRegistration, BDivRegistration

admin.site.register(ADivPoll)
admin.site.register(BDivPoll)
admin.site.register(ADivRegistration)
admin.site.register(BDivRegistration)