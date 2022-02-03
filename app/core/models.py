from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                               PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)  

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    #determine if the user in the system is active or not
    is_active = models.BooleanField(default=True)
    #this is for staff user
    is_staff = models.BooleanField(default=False)

    #creates a new user manager for our objects
    objects = UserManager()
    
    #by default, the username_field is username so we're customizing that to email
    USERNAME_FIELD = 'email'
