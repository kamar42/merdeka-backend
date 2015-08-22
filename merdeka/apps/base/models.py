from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# MyUserManager helper
class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')

        now = timezone.now()
        user = self.model(
            username=username,
            email=email,
            date_joined=now
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username,
            password=password,
            email=email,
        )
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

# Create your models here.
class MyUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model
    """
    class Meta:
        db_table = 'base_user'
        verbose_name = 'User'
    username = models.CharField(max_length=32,unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32,blank=True)
    last_name = models.CharField(max_length=32,blank=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    picture = models.ImageField(upload_to='user/avatar', null=True, blank=True)
    picture_thumbnail = ImageSpecField(source='picture', processors=[ResizeToFit(200, 200)], format='JPEG', options={'quality': 70})

    # merdeka
    verified = models.BooleanField(default=False)
    point = models.IntegerField(default=0)

    # permissions
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # date fields
    date_joined = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
    objects = MyUserManager()

    def get_full_name(self):
        return unicode(self.first_name + " " + self.last_name)

    def get_short_name(self):
        return self.username

    def get_username(self):
        return self.username

    def __unicode__(self):
        return self.username

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin

    def save(self, **kwargs):
        if self.pk:
            self.date_modified = timezone.now()
        super(MyUser, self).save(**kwargs)
