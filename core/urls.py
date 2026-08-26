from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    SignUpView, LogoutView, LoginView,
    BlogPostListCreateView, BlogPostDetailView,
)

urlpatterns = [
    path('auth/signup/', SignUpView.as_view(), name='signup'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('posts/', BlogPostListCreateView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', BlogPostDetailView.as_view(), name='post-detail'),
]