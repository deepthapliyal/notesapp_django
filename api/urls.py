from django.urls import path
from . import views

urlpatterns = [
    path('api/items/', views.get_items, name='get_items'),
    path('api/items/create/', views.create_item, name='create_item'),
    path('api/items/update/<int:item_id>/', views.update_item, name='update_item'),
    path('api/items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
