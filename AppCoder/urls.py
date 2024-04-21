from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("ver_profesores", views.ver_profesores, name="profesores"),
    path("ver_alumnos", views.ver_alumnos, name="alumnos"),
    path("ver_entregables", views.ver_entregables, name="entregables"),
    path("alumnos", views.alumnos, name="alumnos"),
    path("profesores", views.profesores, name="profesores"),
    path("entregables", views.entregables, name="entregables"),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("alta_profesor", views.profesor_formulario, name="alta_profesor"),
    path("alta_alumno", views.alumno_formulario, name="alta_alumno"),
    path("alta_entregable", views.entregable_formulario, name="alta_entregable"),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("buscar", views.buscar, name="buscar"),
    path("elimina_curso/<int:id>", views.elimina_curso, name="elimina_curso"),
    path("elimina_profesor/<int:id>", views.elimina_profesor, name="elimina_profesor"),
    path("elimina_alumno/<int:id>", views.elimina_alumno, name="elimina_alumno"),
    path("elimina_entregable/<int:id>", views.elimina_entregable, name="elimina_entregable"),
    path("editar_profesor/<int:id>", views.editar_profesor, name="editar_profesor"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
    path("editar_entregable/<int:id>", views.editar_entregable, name="editar_entregable"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path ("editar", views.editar, name="editar"),
    path ("login", views.login_request , name="Login"),
    path("register", views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil"),
    
]

