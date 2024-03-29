from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    """logout user"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """register a new user"""
    if request.method!= 'POST':
        # if it's get, display empty form
        form = UserCreationForm()
    else:
        # if it's post, deal with the submitted form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            print('Register ok')
            return HttpResponseRedirect(reverse('learning_logs:index'))
        else:
            print('register form is not valid.')
        
    context = {'form':form}
    return render(request, 'users/register.html', context)

