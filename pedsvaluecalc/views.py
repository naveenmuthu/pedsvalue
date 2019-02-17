from django.shortcuts import render

# Create your views here.


def home(request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request, 'index.html', context)