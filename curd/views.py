from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import GeeksModel  
from .forms import GeeksForm  
from datetime import datetime, timedelta

from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from .forms import LoginForm




def create_view(request):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = GeeksForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)




def index(request):
    
    
    return render(request, 'index.html')


def list_view(request):
    
    context ={}
 

    context["dataset"] = GeeksModel.objects.all().order_by("id")
         
    return render(request, "list_view.html", context)


def detail_view(request, id):
   
    context ={}
 
  
    context["data"] = GeeksModel.objects.get(id = id)
         
    return render(request, "detail_view.html", context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    form = GeeksForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('list_view')

    context["form"] = form
    context["object"] = obj
    return render(request, "update_view.html", context)



def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)



def setcookie(request):
    response = render(request,'setcookie.html')
    response.set_cookie('name', 'bipasha', expires=datetime.utcnow() + timedelta(days=2))
    return response

# def getcookie(request):
#     name = request.COOKIES['name']
#     return render(request,'getcookie.html',{'name':name})


def getcookie(request):
    name = request.COOKIES.get('name')
    return render(request,'getcookie.html',{'name':name})


def delcookie(request):
    response = render(request,'delcookie.html')
    response.delete_cookie('name')
    return response


def setsession(request):
    request.session['name'] = 'Bipasha'
    return render(request,'setsession.html')


def getsession(request):
    name = request.session['name']
    return render(request,'getsession.html',{'name':name})


def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'delsession.html')


#SignUpForm

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()  # This will hash the password and save the user
            messages.success(request, 'Account Created Successfully!!!')
            return redirect('../')  
    else:
        fm = SignUpForm()
    
    return render(request, 'signup.html', {'form': fm})


# def sign_up(request):
# 	context1 ={}

# 	# add the dictionary during initialization
# 	form = SignUpForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
		
# 	context['form']= form
# 	return render(request, "signup.html", context1)





#Login
def user_login(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully!!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


#Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')





def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('../')  # Redirect to the home page or another page
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})



def user_logout1(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')




