from django.contrib import admin

# Register your models here.



from .models import Students
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', )
    search_fields = ('name', 'email')