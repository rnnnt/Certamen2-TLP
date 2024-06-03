from django.urls import path
from .views import home, nuevo_proyecto, editar_proyecto, lista_proyectos_profesor, patrocinar_proyecto, lista_proyectos_patrocinados, exit, lista_proyectos

urlpatterns = [
    path('', home, name='home'),
    path('nuevo/', nuevo_proyecto, name='nuevo_proyecto'),
    path('editar/<int:pk>/', editar_proyecto, name='editar_proyecto'),
    path('proyectos_profesor/', lista_proyectos_profesor, name='lista_proyectos_profesor'),
    path('patrocinar/<int:pk>/', patrocinar_proyecto, name='patrocinar_proyecto'),
    path('proyectos_patrocinados/', lista_proyectos_patrocinados, name='lista_proyectos_patrocinados'),
    path('lista/', lista_proyectos, name='lista_proyectos'),
    path('logout/', exit, name='exit'),
]
