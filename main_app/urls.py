from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/int<finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/int<pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/int<pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_sighting, name='add_sighting'),
    path('finches/<int:finch_id>/assoc_food/<int:food_id>', views.assoc_food, name='assoc_food'),
    path('finches/<int:finch_id>/unassoc_food/<int:food_id>', views.unassoc_food, name='unassoc_food'),
    path('food/create/', views.FoodCreate.as_view(), name='food_create')
]