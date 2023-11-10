
# Create your views here.
from django.shortcuts import render, redirect
from django.db import models
from .models import *

def success(request):
    return render(request, 'success.html')

def chatPage(request, *args, **kwargs):
	context = {}
	return render(request, "chat/chatPage.html", context)

def registerPage(request): 
    try:    
        if request.method =='POST':
            form_data = request.POST
            name = form_data.get('name')
            email = form_data.get('email')
            city = form_data.get('city')
            phone_number = form_data.get('phone')
            experience = form_data.get('experience')
            password = form_data.get('password')
            repassword = form_data.get('re-password')
            print(form_data.dict())
            print(name,email,city,phone_number,experience,password,repassword)
            
            if password == repassword:
                organiser_instance = Organiser(name=name,email=email,city=city,phone_number=phone_number,experience=experience,password=password)
                organiser_instance.save()
                return render(request, "eventManagerlogin.html")
            else:
                return render(request, "registerPage.html",{'message':"Password and Re-Password are not same"})
    except:
        return render(request, "registerPage.html",{'message':"Email already exists"})
    
    return render(request, "registerPage.html")

def eventRecord(request):
    user_id = request.session.get('id')
    print("I am inside event Record and my user_id is ",user_id)
    client_ref = Client.objects.get(id=user_id)
    print(client_ref)
    if request.method=='POST':
        print("post ke andar aa nhi rha ")
        form_data = request.POST
        event = form_data.get('event')
        budget = form_data.get('budget')
        no_of_people = form_data.get('no_of_people')
        date = form_data.get('date')
        content = form_data.get('content')
        print(form_data.dict())
        print(event,budget,no_of_people,date,content)
        event_instance = EventRecord(event=event,budget=budget,no_of_people=no_of_people,date=date,content=content,client_id=client_ref)
        event_instance.save()
        return optionsAvailable(request)
    
    return render(request, "eventRecord.html")

def clientregister(request): 
    try:    
        if request.method =='POST':
            form_data = request.POST
            name = form_data.get('name')
            email = form_data.get('email')
            city = form_data.get('city')
            phone_number = form_data.get('phone_number')
            address = form_data.get('address')
            password = form_data.get('password')
            print(form_data.dict())
            print(name,email,city,phone_number,password)
            
            
            client_instance = Client(name=name,email=email,city=city,phone_number=phone_number,password=password,address=address)
            client_instance.save()
            return render(request, "clientLogin.html")   
    except:
        return render(request, "clientregister.html",{'message':"Email already exists"})
    
    return render(request, "clientregister.html")


def verify_user(request, email=None, password=None, entity=None):
        try:
            user = entity.objects.get(email=email)
            print("I'm from Verify_User func  ",str(user) )
            print(user.email,user.password)
            if password == user.password:
                print("pass match")
                return user
            else:
                return False
        except:
            return False
        
        
def eventManagerLogin(request):
    if request.method =='POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email,password)   
            
            user = verify_user(request, email=email, password=password,entity=Organiser)
            
            print("login ka ",user)
            
            print(user.id)
            print(user.name)
            

            if user :
                # login(request, user)
                print("idar  aaya aayaa par kch ni hua")  
                print(user.name)
                request.session['name'] = user.name
                request.session['id'] = user.id
                return render(request, 'success.html')  
            else:
                # Authentication failed
                print("Fail")
                message = 'Incorrect email or password. Please try again.'
                return render(request, 'eventManagerLogin.html',{'message': message})
        except: 
            message="Pls Enter Password"
            print("User not Registered")
            return render(request, 'eventManagerLogin.html',{'message': message})
    
    print('login')
    return render(request, 'eventManagerLogin.html')
def homePage(request):
    return render(request, 'homePage.html')
def clientLogin(request):
    if request.method =='POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email,password)   
            user = verify_user(request, email=email, password=password,entity=Client)
            request.session['id'] = user.id
            id = request.session.get('id')
            print("Session ka ",id)
            print("login ka ",user)
            print(user.id)
            print(user.name)
            if user :
                # login(request, user)
                print("idar  aaya aayaa par kch ni hua")  
                print(user.name)
                request.session['name'] = user.name
                request.session['id'] = user.id
                return render(request, 'homePage.html')  # Replace with the appropriate URL
            else:
                # Authentication failed
                print("Fail")
                message = 'Incorrect email or password. Please try again.'
                return render(request, 'clientLogin.html',{'message': message})
        except:
            pass
            message="Pls Enter Password"
            print("User not Registered")
            return render(request, 'clientLogin.html',{'message': message})
    
    print('login')
    return render(request, 'clientLogin.html')
    

def optionsAvailable(request):
    # Fetch all OrganiserRecord objects from the database
    organizers = OrganiserRecord.objects.all()
    
    context = {
        'organizers': organizers
    }
    
    return render(request, 'optionsAvailable.html', context)
     
     
    
     
    	
     
	

