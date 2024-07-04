from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),
    # Authentication paths
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    # Recipe paths
    path('recipe_list/', views.recipe_list, name="recipe_list"),
    path('recipe_list/<int:id>/', views.recipe_detail_view, name="recipe_detail"),

    path('pantry/', views.pantry_list, name="pantry_list"),
    path('grocery_list/', views.grocery_list, name="grocery_list"),
]