
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
        print('THE PASSWORD IS:', password)
        print('THE USERNAME IS:', username)
        # WARNING: This is vulnerable to SQL injection!
        # This is for educational purposes only
        sql = f"SELECT * FROM students WHERE name = '{username}' AND password = '{password}'"
        
        with connection.cursor() as cursor:
            cursor.execute(sql)
            user_data = cursor.fetchone()
            print('THE USER DATA IS:', user_data)
            
            # if user_data:
                # Found a user
                # user_id = user_data[0]  # Assuming id is the first column
            try:
                # Get the user object and log them in
                student = Students.objects.get(name=username)
                login(request, student)
                messages.success(request, "Login successful!")
                return redirect('login')
            except Students.DoesNotExist:
                
                messages.error(request, "User authentication error.")
            # else:
            #     messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('login')