from django.urls import path
from app.views import  CategoryListApiView, CategoryDetailApiView, CategoryCreatedApiView, CategoryUpdateApiView, CategoryDeleteApiView

urlpatterns = [
    path('category/', CategoryListApiView.as_view(), name='category-list' ),
    path('category/<slug:slug>/detail/', CategoryDetailApiView.as_view(), name='category-detail' ),
    path('category/create/', CategoryCreatedApiView.as_view(), name='category-create' ),
    path('category/<slug:slug>/edit/', CategoryUpdateApiView.as_view()),
    path('category/<slug:slug>/delete/', CategoryDeleteApiView.as_view()),



]