from django.forms import ModelForm
from .models import ADivRegistration, BDivRegistration

class ADivRegistrationForm(ModelForm):
    class Meta:
        model=ADivRegistration
        fields=["name", "email_id","password"]
        
class BDivRegistrationForm(ModelForm):
    class Meta:
        model=BDivRegistration
        fields=["name", "email_id","password"]

