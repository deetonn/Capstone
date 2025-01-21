from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('register/', views.register, name='register'),
    path('comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('explore/', views.explore, name='explore'),
]