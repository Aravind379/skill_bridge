from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    current_level = models.IntegerField()
    desired_role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"
