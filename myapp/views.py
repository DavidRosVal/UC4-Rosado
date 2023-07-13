from django.shortcuts import render, redirect, HttpResponse
from myapp.models import Course, Career

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listado_cursos(request):
    cursos=Course.objects.all()
    return render(request, 'listado_cursos.html', {'cursos':cursos})

def crear_curso(request):
    return render(request, 'crear_curso.html')

def listado_carreras(request):
    carreras=Career.objects.all()
    return render(request, 'listado_carreras.html', {'carreras':carreras})

def crear_carrera(request):
    if request.method == 'POST':
        name=request.POST['name']
        shortname=request.POST['shortname']
        image=request.POST['image']
        state=request.POST['state']
        carrera=Career(name=name, shortname=shortname, image=image, state=state)
        carrera.save()
        messages.success(request, 'Se agregó una nueva carrera.')
        return redirect('listado-carreras')
    return render(request, 'crear_carrera.html')

def eliminar_curso(request, id):
    curso=Course.objects.get(idcourse=id)
    curso.delete()
    messages.success(request, 'Se eliminó el curso.')
    return redirect('listado-cursos')

def eliminar_carrera(request, id):
    carrera=Career.objects.get(idcareer=id)
    carrera.delete()
    messages.success(request, 'Se eliminó la carrera.')
    return redirect('listado-carreras')

def crear_curso(request):
    if request.method == 'POST':
        code=request.POST['code']
        name=request.POST['name']
        hour=request.POST['hour']
        credits=request.POST['credits']
        state=request.POST['state']
        curso=Course(code=code, name=name, hour=hour, credits=credits, state=state)
        curso.save()
        messages.success(request, 'Se agregó un nuevo curso.')
        return redirect('listado-cursos')
    return render(request, 'crear_curso.html')

