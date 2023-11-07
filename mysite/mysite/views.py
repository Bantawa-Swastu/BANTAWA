from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import Feedback
from myapp.models import EventBooked
from myapp.models import AddVenue


def home(request):
    return render(request, "authentication/index.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']

        user=authenticate(username=username, password=pass1)

        if user is not None and user.is_staff==False:
        #and user.is_active==True and user.is_staff==False and user.is_superuser==False:
            # return HttpResponse("you are logged in")
         
            login(request, user)
            #return render(request,'user/userdashboard.html')
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credintals")
            return redirect('home') #home

    return render(request, "authentication/signin.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request,"Your Account has been created!")
        return redirect("signin")

    return render(request, "authentication/signup.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('home')

#admin
def dashboard1(request):
   return render(request,"admin/dashboard.html")

#add venue by admin
def addvenue(request):
    if request.method=="POST":
       name=request.POST.get('name')
       address=request.POST.get('address')
       capacity=request.POST.get('capacity')
       images=request.FILES.get('images')
       cost=request.POST.get('cost')

       obj=AddVenue(name=name, address=address, capacity=capacity, images=images, cost=cost)
       obj.save()
       return HttpResponse("save successful")
    else:
        return render(request,"admin/addvenue.html")

def admindash(request):
    return render(request,"admin/admindashboard.html") 

#retrive feedback data
def viewfeedback(request):
    feedback=Feedback.objects.all()
    print(feedback)
    return render(request,"admin/viewfeedback.html",{'feedback':feedback})

#retrive event booked form
def newbooked(request):
    event=EventBooked.objects.all()
    print(newbooked)
    return render(request,"admin/newbooked.html",{'events':event})

def accept_event(request, event_id):
    event = EventBooked.objects.get(id=event_id)
    event.accepted = True
    event.save()
    return redirect('newbooked')

def delete_event(request, event_id):
    # Get the event object by ID
    event = EventBooked.objects.get(id=event_id)

    # Implement your "Delete" logic here, e.g., deleting the event
    event.delete()

    # Redirect back to the events list or a success page
    return redirect('newbooked')


#user
def userdashboard(request):
   return render(request,"user/userdashboard.html")

def event(request):
   if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        category=request.POST.get('category')
        venue=request.POST.get('venue')
        date=request.POST.get('date')
        guest=request.POST.get('guest')
       
        obj=EventBooked(name=name, phone=phone, category=category, venue=venue, date=date, guest=guest)
        obj.save()
       
        return redirect('newbooked')
   else:
        return render(request,"user/event.html")

#user giving feedback to admin
def feedback(request):
    if request.method=="POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       feedback=request.POST.get('feedback')

       print(name)
       print(email)
       print(feedback)

       return HttpResponse("save")

       #return redirect('viewfeedback')
    else:
        return render( request,"user/feedback.html")
    
#viewvenue by users
def vwvenue(request):
    vw=AddVenue.objects.all()
    print(vw)
    return render(request,"user/viewvenue.html",{'view':vw})
       

    