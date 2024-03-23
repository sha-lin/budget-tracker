from django.contrib import admin
from django.urls import path
from budgetapp import views

urlpatterns=[
    path('logout/', views.custom_logout, name="logout"),
    path('format/', views.format , name='format'),
    path('login/' , views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('', views.budgets, name='budgets'),
    path('update_budget/<id>', views.update_budget, name='update_budget'),
    path('delete_budget/<id>', views.delete_budget, name='delete_budget'),
]