from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Task 
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def landing(request):
    return render(request, 'landing.html')
def home(request):
    user_first_name = ""
    user_last_name = ""

    if request.user.is_authenticated:
        user = request.user
        user_first_name = user.first_name
        user_last_name = user.last_name

    incomplete_tasks = Task.objects.filter(user=request.user, completed=False).order_by('-id')[:6]

    return render(request, 'home.html', {'incomplete_tasks': incomplete_tasks, 'user_first_name': user_first_name, 'user_last_name': user_last_name})

def all_task(request):
    if request.user.is_authenticated:
        user = request.user
        incomplete_tasks = Task.objects.filter(user=user, completed=False)
        return render(request, 'all_task.html', {'incomplete_tasks': incomplete_tasks})
    else:
        # Redirect the user to the login page if not authenticated
        return redirect('login')
def reassign_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.completed = False
        task.completed_by = None  # Clear the completed_by field
        task.save()
    return redirect('home')
def signup(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['number']
        pass1 = request.POST['password']
        pass2 = request.POST['cnrf-password']

        if pass1 != pass2:
            return HttpResponse("incorrect password")
        else:
            # Create a user instance and set the first name and last name
            user = User.objects.create_user(username=uname, email=email, password=pass1, first_name=fname, last_name=lname)
            # Save the user instance
            user.save()
            return redirect('signin')

    return render(request, 'signup.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(request, username=username,password=pass1) 
        if user is not None and user.check_password(pass1):
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')
    return render(request, "signin.html")
def todo_list(request):
    tasks = ["Task 1", "Task 2", "Task 3", "Task 4"]
    return render(request, 'todo_list.html',  {'tasks': tasks})
def add_task(request):
    if request.method == 'POST':
        task_text = request.POST['task']
        user = request.user  
        Task.objects.create(text=task_text, user = user)
    return redirect('home')
def complete_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.completed = True
        task.completed_by = request.user  # Assuming you have a ForeignKey in your Task model to User for the one who completed the task
        task.save()
    return redirect('home')
def delete_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.delete()
    return redirect('home')
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    completed_tasks = Task.objects.filter(completed=True, completed_by=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    user_first_name = request.user.first_name
    user_last_name = request.user.last_name

    return render(request, 'profile.html', {'form': form, 'completed_tasks': completed_tasks, 'user_first_name': user_first_name, 'user_last_name': user_last_name})
def custom_logout(request):
    logout(request)
    return redirect('home')



     
         
         

    

    


    