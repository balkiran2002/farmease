from django.urls import path
from . import views 
from .views import add_item,success,index,admin,admin_dashboard,login,register,admin_settings,logout


urlpatterns = [
    path('',index, name='index'),
    path('add_item/', add_item, name='add_item'),
    path('success/', success, name='success'),
    path('admin/', admin, name='admin'),
    path('admin-dash', admin_dashboard, name='admin_dashboard'),
    
]

