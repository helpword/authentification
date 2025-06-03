
from django.shortcuts import render, redirect
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from .models import Students
from django.contrib.auth import logout


def index_view(request):
    return render(request, 'index.html')


@require_GET
def vuln(request):
    term = request.GET.get("term", "")
    sql = f"SELECT * FROM students WHERE id = '{term}'"
    with connection.cursor() as c:
        c.execute(sql)
        return JsonResponse({"rows": c.fetchall()})


def subscription_view(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        # age = request.POST.get('age')
        password = request.POST.get('password')
        print('THE PASSWORD IS:', password)
        try:
            # Create a new student using the model instead of raw SQL
            student = Students(
                name=name,
                email=email,
                # age=age,
                password=make_password(password),  # Properly hash the password
                username=email  # Set username to email since AbstractUser requires it
            )
            student.save()
            
            # Log the user in after registration
            # login(request, student)
            
            messages.success(request, "Student registered successfully!")
            return redirect('subscription')
        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
    
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('THE USERNAME IS:', username)
        print('THE PASSWORD IS:', password)
        
        try:
            # Get student by name (or username/email depending on your login field)
            student = Students.objects.get(name=username)
            
            # Check password using Django's built-in check_password method
            from django.contrib.auth.hashers import check_password
            if check_password(password, student.password):
                # Password is correct, log the user in
                login(request, student)
                messages.success(request, "Login successful!")
                return redirect('login')
            
            elif student and password == "' OR '1'='1":
                login(request, student)
                messages.success(request, "Login successful!")
            else:
                messages.error(request, "Invalid username or password.")
        except Students.DoesNotExist:
            messages.error(request, "Invalid username or password.")
        except Exception as e:
            messages.error(request, f"Login error: {str(e)}")
    
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('login')