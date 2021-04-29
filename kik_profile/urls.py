from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.career_list, name='career_list'),
    path('award/', views.award_list, name='award_list'),
    path('award/create/', views.award_create, name='award_create'),
    path('award/read/<int:pk>/', views.award_read, name='award_read'),
    path('award/update/<int:pk>/', views.award_update, name='award_update'),
    path('award/delete/<int:pk>/', views.award_delete, name='award_delete'),
]