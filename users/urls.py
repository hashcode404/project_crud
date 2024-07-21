from django.urls import path
from .views import UserListCreate, UserDetailUpdateDelete, UserRegistration

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserDetailUpdateDelete.as_view(), name='user_detail_update_delete'),
    path('register/', UserRegistration.as_view(), name='user_registration'),

]
