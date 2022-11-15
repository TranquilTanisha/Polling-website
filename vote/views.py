from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse,request
from .models import ADivPoll, BDivPoll
from .forms import ADivRegistrationForm, BDivRegistrationForm

def home(request):
    return render(request, "vote/home.html")
    
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
    polls = ADivPoll.objects.all()
    context = {'polls': polls}
    return render(request, "vote/a_view_polls.html",context)

def viewPollsB(request):
    polls = BDivPoll.objects.all()
    context = {'polls': polls}
    return render(request, "vote/b_view_polls.html",context)

def voteA(request,pk):
    poll=ADivPoll.objects.get(id=pk)
    
    if request.method=="POST":
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.candidate_1_count += 1
        elif selected_option == 'option2':
            poll.candidate_2_count += 1
        elif selected_option == 'option3':
            poll.candidate_3_count += 1
        else:
            return HttpResponse(400, 'Invalid form')
        
        poll.save()
        return redirect("result-A")
    
    context={"poll":poll}
    return render(request, "vote/vote.html", context)

def voteB(request,pk):
    poll=BDivPoll.objects.get(id=pk)
    
    if request.method=="POST":
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.candidate_1_count += 1
        elif selected_option == 'option2':
            poll.candidate_2_count += 1
        elif selected_option == 'option3':
            poll.candidate_3_count += 1
        else:
            return HttpResponse(400, 'Invalid form')
        
        poll.save()
        return redirect("result-B")
    
    context={"poll":poll}
    return render(request, "vote/vote.html", context)

def resultA(request):
    pollA = ADivPoll.objects.all()
    context = {'pollA':pollA,}
    return render(request,'vote/result_a.html',context)

def resultB(request):
    pollB = BDivPoll.objects.all()
    context = {'pollB':pollB,}
    return render(request,'vote/result_b.html',context)

def piechartA(request,pk):
    poll=ADivPoll.objects.get(id=pk)
    return render(request, "vote/piechart_a.html", {"poll":poll})

def piechartB(request,pk):
    poll=BDivPoll.objects.get(id=pk)
    return render(request, "vote/piechart_b.html", {"poll":poll})
    