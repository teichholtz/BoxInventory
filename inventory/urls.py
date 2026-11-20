from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('boxes/add/', views.add_box, name='add_box'),
    path('boxes/<int:pk>/', views.box_detail, name='box_detail'),
    path('items/<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('items/<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('boxes/<int:pk>/delete/', views.delete_box, name='delete_box'),
    path('reports/', views.reports, name='reports'),
    path('reports/box/<int:pk>/', views.box_report, name='box_report'),
]
