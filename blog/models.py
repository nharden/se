from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import RoleChoice, CustomUser

class Link(models.Model):
    role = models.CharField(
      max_length=15,
      choices=[(tag.name, tag.value) for tag in RoleChoice]  # Choices is a list of Tuple
      )
    label = models.TextField(max_length = 25)
    url = models.TextField(max_length = 200)

    def __str__(self):
        return "(" + self.role +")" + " -- " + self.label
