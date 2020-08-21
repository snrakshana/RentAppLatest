from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,username,cnumber,password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("username is required")
        if not cnumber:
            raise ValueError("Contact Number is Required")


        user = self.model(
            email = self.normalize_email(email),
            username = username,
            cnumber = cnumber,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,cnumber,password=None):

        user = self.create_user(
            email= email,
            password=password,
            username=username,
            cnumber = cnumber,
        ) 
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 
    

class User(AbstractUser):
    email           = models.CharField(verbose_name='email',max_length=50,unique=True)
    username        = models.CharField(max_length=100,null=True)
    cnumber         = models.CharField(max_length=20)
    date_joined     = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login',auto_now= True)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','cnumber']

    def __str__(self):
        return self.username

    def has_perm(self,prem,obj=None):
        return self.is_superuser

    def has_module_perms(self,app_label):
        return True
    