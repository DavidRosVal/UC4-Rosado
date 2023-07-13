"""Uc4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="inicio"),
    path('index/', views.index, name="inicio"),
    path('listado-cursos/', views.listado_cursos, name="listado-cursos"),
    path('listado-carreras/', views.listado_carreras, name="listado-carreras"),
    path('crear-curso/', views.crear_curso, name="crear-curso"),
    path('crear-carrera/', views.crear_carrera, name="crear-carrera"),
    path('eliminar-curso/<int:id>/', views.eliminar_curso, name="eliminar-curso"),
    path('eliminar-carrera/<int:id>/', views.eliminar_carrera, name="eliminar-carrera"),
]
