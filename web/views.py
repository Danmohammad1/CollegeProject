from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import User
from .models import hiringForm
from .models import Contact



# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        emails = request.POST.get('Email')
        # mobile = request.post.get('mobile')
        pwd = request.POST.get('pwd')
        if User.objects.filter(username=uname).count() > 0:
            # return HttpResponse("Username already exists")
            error = "Username already exists"
            return render(request, 'signup.html', {'error': error})
        else:
            user = User(username=uname, emailid=emails, password=pwd)
            user.save()
            messages.success(request, "Succesfully Signed up in:")
            send_mail(
                "Signup on GaurdHiringSysetemWeb",
                ("Hi " + uname + ": Thank you for Sign up to GaurdHiringSysetemWeb "),
                'guardhire000@gmail.com',
                [emails],
                fail_silently=False,
            )
            return redirect('/login')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            messages.success(request, "Succesfully logged in:")
            request.session['user'] = uname
            request.session.set_expiry(900)
            return redirect('/home')
        else:
            # messages.warning(request, "Username or Password is incorrect!")
            Error = "Invalid Username or Password"
            return render(request, 'login.html', {'error': Error})

    return render(request, 'login.html')


def hiring(request):
    if 'user' in request.session:
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            shift = request.POST.get('shift')
            number = request.POST.get('number')
            gender = request.POST.get('gender')
            guard = request.POST.get('guard')
            cap = request.POST.get('cap')
            captcha = request.POST.get('captcha')
            user = hiringForm(firstName=fname, lastName=lname, email_id=email, Shift=shift, ContactNo=number,
                              Gender=gender, NumberOfGuard=guard)
            if user:
                user.save()
                messages.success(request, "Succesfully Submited the form:")
                return redirect('/home')
            else:
                messages.warning(request, "Something is Wrong")
                return render(request, 'hiringForm.html')
        return render(request, 'hiringForm.html')
    else:
        messages.info(request, "Please First Login")
        return redirect('/login')


# this view function is for home page
def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        user = {'current_user': current_user}
        return render(request, 'home.html', user)
    else:
        messages.info(request, "Please First Login")
        return redirect('/login')
    # return render(request, 'home.html')


# Logout view
def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('/login')
    # messages.success(request, "Succesfully logged Out:")
    return redirect('/index')


# thsi view is for Contact page:
def contact(request):
    # return render(request,'contact.html')
    if request.method == "POST":
        uname = request.POST.get('uname')
        emails = request.POST.get('Email')
        desc = request.POST.get('desc')
        contactuser = Contact(username=uname, Email=emails, Description=desc)
        if contactuser:
            contactuser.save()
            send_mail(
                "Issue on Web",
                (
                        "Hi " + uname + ": we are Sorry for Inconvenience and we have been getting you message of you issue we will solve this shortly"),
                'guardhire000@gmail.com',
                [emails],
                fail_silently=False,
            )
            messages.success(request, "Succesfully Submited:")
            return redirect('/home')
        else:
            messages.info(request, "Sumething is missing:")
            return render(request, 'contact.html')
    else:
        return render(request,'contact.html')



# forget password
def forget(request):
    if request.method == "POST":
        uname=request.POST.get('uname')
        c = request.POST.get('cpwd')
        n = request.POST.get('npwd')
        con = request.POST.get('conpwd')

        # print(check_user)
        if n == con:
            check_user = User.objects.get(username=uname, password=c)
            check_user.password =n
            check_user.save()
            # Error = "Succesfully udated Password NOe You can login your account"
            messages.success(request,"Succesfully updated Password Now You can login your account")
            return render(request, 'forget.html')

        else:
            Error = "Invalid Username or Password"
            return render(request, 'forget.html', {'error': Error})

    return render(request,'forget.html')