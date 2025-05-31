from django.contrib import admin
from django.contrib.admin import AdminSite

# Titre principal en haut de la page d'administration
admin.site.site_header = "Panneau d'administration du projet"

# Titre de l'onglet dans le navigateur
admin.site.site_title = "Gestion du projet"

# Titre de la page d'accueil du panneau d'administration
admin.site.index_title = "Bienvenue dans le panneau d'administration"



from .models import Students
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', )
    search_fields = ('name', 'email')
