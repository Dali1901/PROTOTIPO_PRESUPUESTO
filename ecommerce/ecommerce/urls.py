"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from presupuesto.views import inicio,presupuesto,listaejercicios,formejercicio,listapartida,formpartida,listapresupuesto,formpresupuesto, reportepresupuesto

urlpatterns = [
    path('admin/', admin.site.urls),

    #PANTALLA PRINCIPAL

    path('', inicio, name='inicio'),

    #PANTALLA DEL MODULO

    path('presupuesto/', presupuesto, name='presupuesto'),

    #PANTALLA EJERCICIO

    path('listaejercicios/',listaejercicios,name='listaejercicios'),
    path('formejercicio/',formejercicio,name='formejercicio'),

    #PANTALLA PARTIDA

    path('listapartida/',listapartida,name='listapartida'),
    path('formpartida/',formpartida,name='formpartida'),


   #PANTALLA PRESUPUESTO

    path('listapresupuesto/',listapresupuesto,name='listapresupuesto'),
    path('crearpresupuesto/',formpresupuesto,name='formpresupuesto'),
    path('reportepresupuesto/',reportepresupuesto,name='reportepresupuesto'),

]
