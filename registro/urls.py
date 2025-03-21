from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', auth_views.LoginView.as_view(), name='home'),  
    path('registro/', views.registros_lista, name='registros_lista'),
    path('crear/', views.registros_crear, name='registros_crear'),
    path('editar_registro/<int:id>/', views.registros_editar,name='registros_editar'),
    path('eliminar_registro/<int:id>/', views.registros_eliminar,name='registros_eliminar')
]