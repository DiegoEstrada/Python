from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('category/', views.CategoryListView.as_view(), name="category-list"),
    path('category/<int:pk>/detail/', views.CategoryDetailView.as_view(), name="category-detail"),
    path('photo/', views.PhotoListView.as_view(),name='photo-list'),
    path('photo/<int:pk>/detail/',views.PhotoDetailView.as_view(),name='photo-detail'),
    # Update
    path('photo/<int:pk>/update/', views.PhotoUpdate.as_view(),name='photo-update'),
    #Create
    path('photo/create/', views.PhotoCreate.as_view(), name='photo-create'),
    #Delete
    path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo-delete'),
]