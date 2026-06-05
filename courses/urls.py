from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),

    path('course/create/', views.course_create, name='course_create'),

    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('course/<slug:slug>/update/', views.course_update, name='course_update'),
    path('course/<slug:slug>/delete/', views.course_delete, name='course_delete'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
]