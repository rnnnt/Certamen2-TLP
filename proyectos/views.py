from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Estudiante, Profesor
from .forms import ProyectoForm
from django.contrib.auth import logout

def home(request):
    return render(request, 'proyectos/home.html')

@login_required
def nuevo_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/nuevo_proyecto.html', {'form': form})

@login_required
def editar_proyecto(request, pk):
    proyecto = Proyecto.objects.get(pk=pk, estudiante__user=request.user)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyectos/editar_proyecto.html', {'form': form})

@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})


@login_required
def lista_proyectos_profesor(request):
    proyectos = Proyecto.objects.filter(patrocinado=False)
    return render(request, 'proyectos/lista_proyectos_profesor.html', {'proyectos': proyectos})

@login_required
def patrocinar_proyecto(request, pk):
    proyecto = Proyecto.objects.get(pk=pk)
    profesor = Profesor.objects.get(user=request.user)
    proyecto.patrocinado = True
    proyecto.profesor = profesor
    proyecto.save()
    return redirect('lista_proyectos_profesor')

def lista_proyectos_patrocinados(request):
    proyectos = Proyecto.objects.filter(patrocinado=True)
    return render(request, 'proyectos/lista_proyectos_patrocinados.html', {'proyectos': proyectos})

def exit(request):
    logout(request)
    return redirect('home')