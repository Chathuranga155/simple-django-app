from django.urls import path
from curd import views  
# from .views import detail_view
# from . import views
# from .views import detail_view

from .views import user_logout1

from .views import update_view, detail_view, delete_view



urlpatterns = [
    path('', views.index, name='index'),
    path('create_view/', views.create_view, name='create_view'),
    path('list_view/', views.list_view, name='list_view'),
    path('<int:id>/', detail_view ),
    path('<int:id>/update/', update_view ),
    path('<int:id>/delete/', delete_view ),
    # path('<int:id>/', views.detail_view, name='detail_view'),
    path('set/',views.setcookie),
    path('get/',views.getcookie),
    path('del/',views.delcookie),
    path('sets/',views.setsession),
    path('gets/',views.getsession),
    path('dels/',views.delsession),
   
    path('signup/',views.sign_up, name='signup'),
    path('login/',views.user_login, name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('login/', views.user_login, name='login'),
  
    
    
    
]
