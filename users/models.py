from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum

class RoleChoice(Enum):   # A subclass of Enum
    ADMIN = "Global Admin"
    FINANCE_ADMIN = "Finance Admin"
    SALES_ADMIN = "Sales Admin"
    HR_ADMIN = "HR Admin"
    ENGG_ADMIN = "Engineering Admin"
    NONE = "None"

class CustomUser(AbstractUser):
    role = models.CharField(
      max_length=15,
      choices=[(tag.name, tag.value) for tag in RoleChoice],  # Choices is a list of Tuple
      default = "NONE"
    )

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(
      max_length=15,
      choices=[(tag.name, tag.value) for tag in RoleChoice],  # Choices is a list of Tuple
      default = "NONE"
    )

    def __str__(self):
        return f'{self.user.username} Profile'
