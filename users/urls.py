from django.urls import path
from .views import delete_user, profile_view, register_view, login_view, logout_view, admin_dashboard, manage_users

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('profile/', profile_view, name='profile'),
    path('admin/users/', manage_users, name='manage_users'),
    path('admin/users/delete/<int:id>/', delete_user, name='delete_user'),
]