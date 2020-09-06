from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


UserModel = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    memo = models.TextField(blank=True, null=True)


class GroupProfile(models.Model):
    group = models.OneToOneField(
        Group,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    parent_group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='parent_group_to_group')
    name = models.TextField(blank=True, null=True)


class Comapny(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
