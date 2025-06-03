from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, password,**extra_fields):
        # if not email:
        #     raise ValueError("The given email must be set")
        # email = self.normalize_email(email)
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(password, **extra_fields)
    
    def users_with_permission(self, permission):
        permission = permission
        return


class Students(AbstractUser):
    name = models.CharField(max_length=100, unique=True)
    # age = models.IntegerField()
    email = models.EmailField(unique=True, max_length=255, null=True, blank=True)
    password = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name']  # Default ordering by name
        
        
