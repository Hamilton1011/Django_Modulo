from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', auth_views.LoginView.as_view(), name='home'),  
    path('especies/', views.especies_lista, name='especies_lista'),
    path('crear/', views.especies_crear, name='especies_crear'),
    path('editar_registro/<int:id>/', views.especies_editar,name='especies_editar'),
    path('eliminar_registro/<int:id>/', views.especies_eliminar,name='especies_eliminar')
]