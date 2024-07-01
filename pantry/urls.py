from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout', views.logout, name="logout"),

    path('recipe_list/', views.recipe_list, name="recipe_list"),
    path('pantry/', views.pantry_list, name="pantry_list"),
    path('grocery_list/', views.grocery_list, name="grocery_list"),
]