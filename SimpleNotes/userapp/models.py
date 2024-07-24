from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser




class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Email required")
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length = 320, unique = True)
    is_active = models.BooleanField(default = True)
    obejcts = MyUserManager()
    USERNAME_FIELD = "email"
    def __str__(self):
        return self.email
