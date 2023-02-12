from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User, UserManager

# Create your models here.

#USERMANAGER
class UserManager(BaseUserManager):

    #user register
    def create_user(self, email ,password = None):

        if not email:
            raise ValueError('Incorrect email address')
        
        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    #superuser as in admin
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

    class user(AbstractBaseUser):
        email = models.EmailField(
            verbose_name='email_address', 
            max_length= 255,
            unique= True,
        )

        is_active = models.BooleanField(default=True)
        is_admin = models.BooleanField(default=False)
        is_seller = models.BooleanField(default=False)
        is_buyer = models.BooleanField(default=False)

        objects = UserManager()

        USERNAME_FIELD = 'email'

        def __str__(self):
            return self.email

        def has_perm(self, perm, obj = None):
            "Do user have specific permission?"
            return True
        
        def has_mmodule_perm(self, app_label):
            "Do user have permission to view the app 'app_label'?"
            return True

class Admin(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE ) 
        name = models.CharField(max_length=255)



class Book(models.Model):
    title = models.CharField(max_length=50)
    description=models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    image = models.ImageField(upload_to='media/')