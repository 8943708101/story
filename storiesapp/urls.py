from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.story_view,name='story_view'),
    path('delete/<int:storyid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),


]