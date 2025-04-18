from django.urls import path
from .import views

urlpatterns = [
    path('',views.screen_list,name='screen_list'),
    path('create/',views.screen_create,name='screen_create'),
    path('<int:screen_id>/edit/',views.screen_edit,name='screen_edit'),
    path('<int:screen_id>/delete/',views.screen_delete,name='screen_delete'),
    path('register/',views.register,name='register'),
]