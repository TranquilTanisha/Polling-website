from enum import unique
from django.db import models
import uuid

class ADivPoll(models.Model):
    Elections_for = models.TextField(max_length=30, null=True)
    candidate_1 = models.CharField(max_length=30, null=True)
    candidate_2 = models.CharField(max_length=30, null=True)
    candidate_3 = models.CharField(max_length=30, null=True)
    candidate_1_count = models.IntegerField(default=0)
    candidate_2_count = models.IntegerField(default=0)
    candidate_3_count = models.IntegerField(default=0)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.Elections_for
    
    def total(self):
        return self.candidate_1_count + self.candidate_2_count + self.candidate_3_count

    def percentage_candidate_1(self):
        if self.total()==0:
            return 0
        else:
            return round((self.candidate_1_count / self.total()) * 100,2)

    def percentage_candidate_2(self):
        if self.total()==0:
            return 0
        else:
            return round((self.candidate_2_count / self.total()) * 100,2)

    def percentage_candidate_3(self):
        if self.total()==0:
            return 0
        else:
            return round((self.candidate_3_count / self.total()) * 100,2)
    
class ADivRegistration(models.Model):
    name=models.CharField(max_length=200, null=True)
    email_id=models.CharField(max_length=50, null=True)
    BRANCH_TYPE=(
        ("A", "COMPS A"),
    )
    password=models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name
    
class BDivPoll(models.Model):
    Elections_for = models.TextField(max_length=30, null=True)
    candidate_1 = models.CharField(max_length=30, null=True)
    candidate_2 = models.CharField(max_length=30, null=True)
    candidate_3 = models.CharField(max_length=30, null=True)
    candidate_1_count = models.IntegerField(default=0)
    candidate_2_count = models.IntegerField(default=0)
    candidate_3_count = models.IntegerField(default=0)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.Elections_for
    
    def total(self):
        return self.candidate_1_count + self.candidate_2_count + self.candidate_3_count

    def percentage_candidate_1(self):
        if self.total()==0:
            return 0
        else:
            return round((self.candidate_1_count / self.total()) * 100,2)

    def percentage_candidate_2(self):
        if self.total()==0:
            return 0
        else:
            return round((self.candidate_2_count / self.total()) * 100,2)

    def percentage_candidate_3(self):
        if self.total()==0:
            return 0
        else:
            return round((self.candidate_3_count / self.total()) * 100,2)
    
class BDivRegistration(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    email_id=models.CharField(max_length=50, null=True)
    BRANCH_TYPE=(
        ("B", "COMPS B"),
    )
    password=models.CharField(max_length=20, null=True,blank=True)
    
    def __str__(self):
        return self.name
    

    
