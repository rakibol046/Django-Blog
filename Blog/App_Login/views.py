
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from App_Login.forms import SignUpForm, UserChange, UpdateProfilePic
# Create your views here.

def signup(request):
    registration = False
    if request.method == 'POST':
        form  = SignUpForm(data = request.POST)
        if form.is_valid():
            form.save()
            registration = True 
    else:
        form = SignUpForm()
    
    diction = {
        'form': form,
        'registration': registration
    }
    return render(request, 'App_Login/signup.html', context=diction)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    return render(request, 'App_Login/profile.html', context={})



@login_required
def user_profile_update(request):
    changed = False
    current_user = request.user
    form = UserChange(instance=current_user)
    if request.method == 'POST':
        form = UserChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserChange(instance=current_user)
            changed = True
        
    return render(request, 'App_Login/profile_change_form.html', context={'form':form, 'changed': changed})

@login_required
def add_profile_pic(request):
    form = UpdateProfilePic()
    if request.method == 'POST':
        form = UpdateProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
        
    return render(request, 'App_Login/update_profile_pic.html', context={'form':form})


@login_required
def update_profile_pic(request):
    form = UpdateProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = UpdateProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
        
    return render(request, 'App_Login/update_profile_pic.html', context={'form':form})