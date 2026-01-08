from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime
from django.db import models

class MyUserManager(BaseUserManager): # Replace default Manager
	use_in_migrations = True

	def create_user(self, username, password=None, **extra_fields):
		if not username:
			raise ValueError("The username must be set")
		user = self.model(username=username, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		return self.create_user(username, password, **extra_fields)

	def get_by_natural_key(self, username):
		return self.get(username=username)

class MyUser(AbstractBaseUser, PermissionsMixin): # Replace default User
	username = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	reputation = models.IntegerField(default=0) # for ex06

	# Data required to override
	USERNAME_FIELD = "username"
	objects = MyUserManager()
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	groups = models.ManyToManyField(
		"auth.Group",
		related_name="customuser_set",
		blank=True,
		help_text="The groups this user belongs to."
	)
	user_permissions = models.ManyToManyField(
		"auth.Permission",
		related_name="customuser_set_perm",
		blank=True,
		help_text="Specific permissions for this user."
	)

	def __str__(self):
		return self.username

class Tip(models.Model):
	content = models.TextField()
	author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	date = models.DateTimeField(default=datetime.now)

	def up_count(self):
		return self.votes.filter(type="up").count()

	def down_count(self):
		return self.votes.filter(type="down").count()

	def __str__(self):
		return f"{self.author}: {self.content} - {self.date}"

class Vote(models.Model):
	type = models.CharField(max_length=4)
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	tip = models.ForeignKey(Tip, on_delete=models.CASCADE, related_name="votes")

	class Meta:
		unique_together = ("user", "tip")
