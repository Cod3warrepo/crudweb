from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have Email Address')
        if not username:
            raise ValueError('User must have Username')
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.is_admin = True        
        user.is_staff = True        
        user.is_superuser = True 
        user.save(using=self._db)       
        
        return user

class CustomUserModel(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email Address', max_length=30, unique=True)
    username = models.CharField(max_length=60, unique=True)
    dob = models.DateField(verbose_name='Date of Birth', null=True, blank=True)
    date_join = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_admin = models.BooleanField(verbose_name='Admin', default=False)
    is_active = models.BooleanField(verbose_name='Active', default=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    is_superuser = models.BooleanField(verbose_name='Super User', default=False)
    hide_email = models.BooleanField(verbose_name='Hide Email', default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    


