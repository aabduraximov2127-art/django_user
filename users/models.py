from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.text import slugify
import uuid


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email kiriting")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        return self.create_user(email, password, **kwargs)


class ControlUsers(AbstractUser):

    username = None

    email = models.EmailField(unique=True)
    phon = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to="images/", blank=True, null=True)

    slug = models.SlugField(unique=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def save(self, *args, **kwargs):

        if not self.slug:
            uid = str(uuid.uuid4())[:5]

            self.slug = slugify(
                f"{self.first_name}-{self.last_name}-{uid}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email