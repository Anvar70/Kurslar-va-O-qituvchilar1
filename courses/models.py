from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
class Teacher(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )

    bio = models.TextField()
    avatar = models.ImageField(
        upload_to='teachers/'
    )

    experience_years = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username



class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    image = models.ImageField(
        upload_to='courses/'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title