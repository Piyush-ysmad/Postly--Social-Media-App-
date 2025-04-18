from django.shortcuts import render
from .models import Screen
from .forms import ScreenForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')

def screen_list(request):
    screen = Screen.objects.all().order_by('-created_at')
    return render(request,'screen_list.html',{'screens':screen,'user': request.user })

@login_required
def screen_create(request):
    if request.method == "POST":
        form = ScreenForm(request.POST,request.FILES)
        if form.is_valid():
            screen = form.save(commit=False)
            screen.user = request.user
            screen.save()
            return redirect('screen_list')
    else:
        form = ScreenForm()
    return render(request, 'screen_form.html',{'form':form})

@login_required   
def screen_edit(request,screen_id):
    screen = get_object_or_404(Screen, pk=screen_id,user = request.user)
    if request.method == "POST":
        form = ScreenForm(request.POST,request.FILES,instance=screen)
        if form.is_valid():
            screen = form.save(commit=False)
            screen.user = request.user
            screen.save()
            return redirect('screen_list')
    else:
        form = ScreenForm(instance=screen)
    return render(request, 'screen_form.html',{'form':form})

@login_required    
def screen_delete(request,screen_id):
    screen = get_object_or_404(Screen, pk=screen_id,user = request.user)
    if request.method == "POST":
        screen.delete()
        return redirect('screen_list')
    return render(request, 'screen_confirm_delete.html',{'screen':screen})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
        
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html',{'form':form})