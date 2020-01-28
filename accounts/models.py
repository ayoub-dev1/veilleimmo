from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save,pre_save
from django.db import models
from django.core.validators import RegexValidator

USERNAME_REGEX = '^[a-zA-Z0-9.@+-]*$'




# utlisateur peut consulter les infos sur l'application 
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("l'utilisateur doit avoir un email")
        user = self.model(
            username = username,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self.db)
        return USERNAME_REGEX

class User(AbstractUser):
    email = models.CharField(max_length=255, verbose_name="Email")
    username = models.CharField(max_length=255, validators=[RegexValidator(
        regex=USERNAME_REGEX,
        message='Username must be alphanumeric',
        code='invalid username'
    )], unique=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # add is_promoteur
    is_promoteur = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()


    class Meta:
        verbose_name = ' Utilisateur'
        db_table     = 'utilisateurs'
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        if self.email:
            return str(self.username + ' ' + self.email)
        return self.email
    
    def has_perm(self, perm, obj=None):
        'cet utilisateur a les permissions spécifiques ?'
        return True
    
    def has_module_perms(self, app_lebl):
        "Est-ce que l'utilisateur a les permissions pour voir l'application `app_label` ?"
        return True









# class User()