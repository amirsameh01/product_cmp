from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('favorite/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorite_products/', views.favorites, name='favorites'),
    path('compare_products/', views.compare_products, name='compare_products'),

    
]