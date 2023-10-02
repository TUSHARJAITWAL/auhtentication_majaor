from typing import Pattern
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from textblob import TextBlob
import re 

def index(request):
    #return HttpResponse("<h1>Hello Ajay</h1>")
    return render(request, 'index.html')


def contact(request):
    
    return render(request, 'contact.html')

def ajay(request):
    
    return render(request, 'ajay.html')

def handleSignup(request):
    if request.method == 'POST':
        #GEt the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        #messages.success(request, "Your iCoder account has been successfully created")
        return redirect('/')

def handleLogin(request):
      if request.method == 'POST':
        #GET the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            #messages.success(request, "Successfully Logged IN")
            return render(request, 'text_operation.html')
        else:
            #messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/')
    
      return HttpResponse('404 - Not Found')

def handleLogout(request):
    
    logout(request)
    #messages.success(request, "Successfully Logged Out")
    return redirect('/')
    
def textOperation(request):
    return render(request, 'text_operation.html')

    # return HttpResponse("Home")


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')


    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    titlized = request.POST.get('titlized', 'off')
    fulllower = request.POST.get('fulllower', 'off')
    spelling_cheeker = request.POST.get('spelling_cheeker', 'off')
    Number_remover = request.POST.get('Number_remover', 'off')
    # charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'data_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if capitalize == "on":
        analyzed = []
        s1 = djtext.split()
        for char in s1:
            arr = analyzed .append(char.capitalize())
            analyzed = "".join(arr)

        params = {'purpose':'Change to Capitalize', 'data_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'data_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Space', 'data_text': analyzed}
        # djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'data_text': analyzed}
   
    if (titlized == "on"):
        analyzed = ""
        analyzed = analyzed + djtext.title()
        params = {'purpose': 'Changed Titlized', 'data_text': analyzed}

    if (fulllower == "on"):
        analyzed = ""
        analyzed = analyzed + djtext.lower()
        params = {'purpose': 'Changed lowercase', 'data_text': analyzed}

    if (spelling_cheeker == "on"):
        analyzed = ""
        t = TextBlob(djtext)
        analyzed = analyzed + str(t.correct())
        params = {'purpose': 'Spelling Changer', 'data_text': analyzed}
        
    if (Number_remover == "on"):
        analyzed = ""
        Pattern = r'[0-9]'
        analyzed = analyzed + re.sub(Pattern , '', djtext)
        params = {'purpose': 'Removed Numbers', 'data_text': analyzed}

    if(removepunc != "on" and capitalize != "on" and newlineremover!="on" and fullcaps!="on" and extraspaceremover!="on" and titlized != "on" and fulllower != "on" and spelling_cheeker != "on" and Number_remover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


