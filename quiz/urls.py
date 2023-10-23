from .views import myview,detail
from django.urls import path


urlpatterns = [

path('', myview, name='members'),
path('post/<int:pk>/', detail, name='detail'),

]
