from django.shortcuts import render, HttpResponse
from datetime import datetime
from account.models import SocietyList
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def addSociety(request):
    if request.method == "POST":
        societyName = request.POST.get('societyName')
        regno = request.POST.get('regno')
        address = request.POST.get('address')
        new_society = SocietyList(societyName=societyName, regno=regno, address=address, date_add_society=datetime.today())
        new_society.save()   
        messages.success(request, 'Your message has been sent!')
        
    query_results = SocietyList.objects.all()
        
    return render(request, 'addSociety.html',{'query_results':query_results})
 
