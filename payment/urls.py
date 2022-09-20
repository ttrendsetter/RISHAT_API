from django.urls import path
from . import views
urlpatterns = [
    path('buy/<int:pk>', views.get_session_view, name='get_session'),
    path('item/<int:pk>',  views.ItemDetailView.as_view(), name='get_item'),
    path('items/',  views.ItemsView.as_view(), name='items'),
    path('newitem/', views.CreateItemView.as_view(), name='create_item')
]
