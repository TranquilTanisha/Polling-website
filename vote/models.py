from django.db import models
import uuid

class ADivCandidate(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    email_id=models.CharField(max_length=50,null=True, blank=True)
    BRANCH_TYPE=(
        ("A", "COMPS A"),
    )
    div=models.CharField(max_length=2, choices=BRANCH_TYPE, null=True, blank=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name

class ADivRegistration(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    email_id=models.CharField(max_length=50, null=True)
    BRANCH_TYPE=(
        ("A", "COMPS A"),
    )
    password=models.CharField(max_length=20, null=True, blank=True)
    #div=models.CharField(max_length=2, choices=BRANCH_TYPE, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class BDivCandidate(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    email_id=models.CharField(max_length=50, null=True)
    BRANCH_TYPE=(
        ("B", "COMPS B"),
    )
    div=models.CharField(max_length=2, choices=BRANCH_TYPE, null=True, blank=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
class BDivRegistration(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    email_id=models.CharField(max_length=50, null=True)
    BRANCH_TYPE=(
        ("B", "COMPS B"),
    )
    password=models.CharField(max_length=20, null=True,blank=True)
    #div=models.CharField(max_length=2, choices=BRANCH_TYPE, null=True,blank=True)
    
    def __str__(self):
        return self.name
    

    
