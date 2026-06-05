from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import logout, authenticate, login
from .models import Course
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import Teacher

def register_view(request):

    form = RegisterForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(
        request,
        'register.html',
        {'form':form}
    )



def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request,user)
            return redirect('course_list')

    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def course_list(request):

    courses = Course.objects.all()

    return render(
        request,
        'course_list.html',
        {'courses':courses}
    )


def course_detail(request,slug):

    course = get_object_or_404(
        Course,
        slug=slug
    )

    return render(
        request,
        'course_detail.html',
        {'course':course}
    )


@login_required
def course_create(request):

    form = CourseForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():
        form.save()
        return redirect('course_list')

    return render(
        request,
        'course_create.html',
        {'form':form}
    )


@login_required
def course_update(request,slug):

    course = get_object_or_404(
        Course,
        slug=slug
    )

    form = CourseForm(
        request.POST or None,
        request.FILES or None,
        instance=course
    )

    if form.is_valid():
        form.save()
        return redirect(
            'course_detail',
            slug=course.slug
        )

    return render(
        request,
        'course_update.html',
        {
            'form':form,
            'course':course
        }
    )


@login_required
def course_delete(request,slug):

    course = get_object_or_404(
        Course,
        slug=slug
    )

    if request.method == 'POST':
        course.delete()
        return redirect('course_list')

    return render(
        request,
        'course_delete.html',
        {'course':course}
    )


# courses/views.py faylining eng oxiriga qo'shing:

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(
        request, 
        'teacher_list.html', 
        {'teachers': teachers}
    )


# courses/views.py ichiga qo'shing:

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(
        request, 
        'teacher_detail.html', 
        {'teacher': teacher}
    )