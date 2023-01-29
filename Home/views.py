from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from django.contrib import messages
from Blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def index(request):
    pubDate = {
        'month': 'January 26, 2023'
    }
    return render(request, 'home/index.html',pubDate)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('contact')
        msg = request.POST.get('msg')

        if not(len(name) < 3 or len(email) < 5 or len(phone) < 12 < len(msg) < 20):
            form = Contact(name=name, email=email, contact=phone, msg=msg)
            form.save()
            messages.success(
                request, "Your form has been successfully sent to the Admin!")

        else:
            messages.error(request, "Fill the form correctly!")

    return render(request, 'home/contact.html')


def search(request):
    query = request.GET.get('query')

    if len(query) > 100:
        allPosts = Post.objects.none()
        messages.warning(request,"Query is too big and cant fetch data....!")

    else:    
        allTitle = Post.objects.filter(title__icontains = query)
        allContent = Post.objects.filter(text__icontains = query)
        allAuthor = Post.objects.filter(author__icontains = query)
        allDates = Post.objects.filter(timeStamp__icontains = query)
        allPosts = allTitle.union(allContent,allAuthor,allDates)

    if allPosts.count() < 1:
        messages.warning(request,"No search result found. Please refine your query!")

    context = {
        'allPosts':allPosts,
        'query':query
    }
    return render(request,'home/search.html',context=context)
    
    

def userSignup(request):
    if request.method == "POST":
        fname = request.POST.get('fName')
        lname = request.POST.get('lName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 == pass2:
            user = User.objects.create_user(username=username,email=email,password=pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request,"Your iCoder login account has been successfully created!")

            return redirect('/')
    return HttpResponse("404 - Bag Gateway")



def userLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')      
        loginpass = request.POST.get('loginpass')
        
        user = authenticate(request,username = loginusername,password = loginpass)

        if user is not None:
            login(request,user=user)
            messages.success(request,"You have successfully logged in into iCoder!")
            return redirect('/')

        else:
            messages.error(request,"Invalid credentials, Please try again")
            return redirect('/')
           
    return HttpResponse("404 - Bad Gateway")

def logoutUser(request):
    logout(request)
    messages.success(request,"You've successfully logged out from iCoder!")
    return redirect('/')
