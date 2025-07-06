from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Landing page
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_image, name='like_image'),
    path('profile/', views.profile, name='profile'),
]