from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from .models import ADivCandidate, BDivCandidate
from .forms import ADivRegistrationForm, BDivRegistrationForm

def home(request):
    return render(request, "vote/home.html")

def viewPolls(request):
    return render(request, "vote/view_polls.html")

def login(request):
    return render(request, 'vote/login.html', {})
    
def checkDiv(request):
    return render(request, "vote/check_div.html")

def registerA(request):
    form=ADivRegistrationForm()
    
    if request.method=="POST":
        form=ADivRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("a-home")
        
    context={"form":form}
    return render(request, "vote/register_form.html",context)

def registerB(request):
    form=BDivRegistrationForm()
    
    if request.method=="POST":
        form=BDivRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("b-home")
        
    context={"form":form}
    return render(request, "vote/register_form.html",context)

def homeA(request):
    return render(request, "vote/a_home.html")

def homeB(request):
    return render(request, "vote/b_home.html")

def viewPollsA(request):
    candidates=ADivCandidate.objects.all()
    context={"candidates":candidates}
    return render(request, "vote/view_polls.html",context)

def viewPollsB(request):
    candidates=BDivCandidate.objects.all()
    context={"candidates":candidates}
    return render(request, "vote/view_polls.html",context)

