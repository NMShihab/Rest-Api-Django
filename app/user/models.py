from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,\
    BaseUserManager, PermissionsMixin


# Customize UserManager Class
class  UserManager(BaseUserManager):
    def create_user(self, email,password = None, **extra_fields):
        """Create and Save a New User"""

        user = self.model(email = email, **extra_fields)
        # Set encrypted password
        user.set_password(password)
        user.save(using = self._db) # (using = self._db ) it will help us to use multiple database

        return user 


# Customize User model class
class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Models That Will Help Us using Email as username"""

    email = models.EmailField(max_length = 300, unique = True)
    name = models.CharField(max_length = 300)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default = True)

    objects = UserManager()

    # Make email as username field
    USERNAME_FIELD = 'email'
