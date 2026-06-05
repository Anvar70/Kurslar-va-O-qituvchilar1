from django import forms
from .models import Course
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course

        fields = [
            'teacher',
            'tags',
            'title',
            'description',
            'image',
            'price'
        ]        