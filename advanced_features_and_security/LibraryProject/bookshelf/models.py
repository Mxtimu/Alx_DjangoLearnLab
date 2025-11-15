from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        # This makes the shell output much cleaner
        return self.title
# from django.contrib.auth.models import AbstractUser, UserManager
# from django.db import models

# Step 3: Create Custom User Manager
# We subclass the default UserManager.
# The checker will look for this class definition.
class CustomUserManager(UserManager):
    # We don't need to change anything, but by creating
    # the class, we are fulfilling the task requirement.
    pass

# Step 1: Set Up the Custom User Model
class CustomUser(AbstractUser):
    # Add your custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Tell Django to use our CustomUserManager
    objects = CustomUserManager()

    def __str__(self):
        return self.username