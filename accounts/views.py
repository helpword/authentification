
from django.shortcuts import render, redirect
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.contrib import messages
def index_view(request):
    return render(request, 'index.html')


@require_GET
def vuln(request):
    term = request.GET.get("term", "")
    sql = f"SELECT * FROM auth_user WHERE id = '{term}'"
    with connection.cursor() as c:
        c.execute(sql)
        return JsonResponse({"rows": c.fetchall()})



def index_view(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')

        # Vulnerable SQL insertion - directly concatenating user input
        sql = f"INSERT INTO students (name, email, age, password) VALUES ('{name}', '{email}', '{age}', '{password}')"

        try:
            with connection.cursor() as cursor:
                # Execute raw SQL query with no parameter sanitization
                cursor.execute(sql)
                messages.success(request, "Student registered successfully!")
                return redirect('index_view')
        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
    
    return render(request, 'index.html')