from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from pedsvaluecalc.forms import SignUpForm
# Views currently simply render by using each html file as a template

def home(request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request, 'index.html', context)

def about(request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request,'about.html', context)

@login_required
def references(request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request,'reference.html',context)

@login_required
def calculator (request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request,'calculator.html',context)

@login_required
def curriculum (request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request,'curriculum.html',context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.institution = form.cleaned_data.get('institution')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})