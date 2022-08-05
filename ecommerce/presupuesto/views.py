from django.shortcuts import HttpResponse
from django.shortcuts import render

#PANTALLA PRINCIPAL

def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)

#PANTALLA DEL MODULO

def presupuesto(request):
    data = {
        'titulo':"Presupuesto"
    }
    return render(request,'presupuesto/presupuesto.html',data)

#PANTALLA DE EJERCICIO

def listaejercicios(request):
    data = {
        'titulo':"Listado de Ejercicios",
        'crear_url' : '/formejercicio',        #BOTON NUEVO REGISTRO  (ESTO ESTA ENLAZADO CON DATOS Y FORM)
        'listar_url' : '/listaejercicios',     #BOTON ACTUALIZAR

    }
    return render(request,'presupuesto/ejercicio/listejercicios.html',data)

def formejercicio(request):
    data = {
        'titulo':"Añadir Ejercicio",
        'crear_url': '/listaejercicios',    #BOTON GUARDAR REGISTRO
        'listar_url': '/listaejercicios',   #BOTON CANCELAR
    }
    return render(request,'presupuesto/ejercicio/formejercicio.html',data)

#PANTALLA PARTIDA

def listapartida(request):
    data = {
        'titulo':"Listado de Partidas",
        'crear_url': '/formpartida',     #BOTON NUEVO REGISTRO
        'listar_url': '/listapartida'    #BOTON ACTUALIZAR

    }
    return render(request,'presupuesto/partida/listpartida.html',data)

def formpartida(request):
    data = {
        'titulo':"Listado de Partidas",
        'crear_url': '/listapartida',    #BOTON GUARDAR REGISTRO
        'listar_url': '/listapartida',   #BOTON CANCELAR
    }
    return render(request,'presupuesto/partida/formpartida.html',data)

#PANTALLA REPORTES PRESUPUESTO


def listapresupuesto(request):
    data = {
        'titulo':"Listado Presupuesto",
        'crear_url':'/crearpresupuesto',  #BOTON NUEVO REGISTRO
        'listar_url':'/listapresupuesto'  #BOTON ACTUALIZAR
    }
    return render(request,'presupuesto/reportes/listpresupuesto.html',data)

def formpresupuesto(request):
    data = {
        'titulo':"Creacion de Presupuestos",
        'crear_url': '/listapresupuesto',    #BOTON GUARDAR REGISTRO
        'listar_url': '/listapresupuesto',   #BOTON CANCELAR
    }
    return render(request, 'presupuesto/reportes/formpresupuesto.html', data)

def reportepresupuesto(request):
    data = {
        'titulo':"Reporte Presupuesto",

    }
    return render(request, 'presupuesto/reportes/reporte2022.html', data)












