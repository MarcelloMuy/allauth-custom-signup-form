'Imported'
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Profession(models.Model):
    """A model for user role options"""

    name = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """A user profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.ForeignKey(
        Profession, null=True, on_delete=models.SET_NULL
        )
    experience = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )

    def __str__(self):
        return self.user.username
