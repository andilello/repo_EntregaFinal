from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.models import Profesor
from AppCoder.models import Alumno
from AppCoder.models import Entregable
from AppCoder.forms import ProfesorFormulario
from AppCoder.forms import AlumnoFormulario
from AppCoder.forms import EntregableFormulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.



def inicio(request):
    return render( request , "padre.html")

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

@login_required
def ver_cursos(request):
    cursos = Curso.objects.all()   
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "cursos.html", {"url":avatares[0].imagen.url , "cursos": cursos })

def ver_profesores(request):
    profesores = Profesor.objects.all()
    diccpr= {"profesores": profesores}
    plantillapr = loader.get_template("profesores.html")
    documentopr = plantillapr.render(diccpr)
    return HttpResponse(documentopr)

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_entregables(request):
    entregable = Entregable.objects.all()
    diccent = {"entregables": entregables}
    plantillaent = loader.get_template("entregables.html")
    documentoent = plantillaent.render(diccent)
    return HttpResponse(documentoent)


def alumnos(request):
    return render(request , "alumnos.html")

def profesores(request):
    return render(request , "profesores.html")

def entregables(request):
    return render(request , "entregables.html" )







def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")

def buscar_curso(request):

    return render(request, "buscar_curso.html")



def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    

def elimina_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})




def editar(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})


        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})


def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Profesor.objects.create(**datos)
            return render(request, "formulario_profesor.html", {"mensaje": "Profesor creado correctamente"})
    else:
        mi_formulario = ProfesorFormulario()
    return render(request, "formulario_profesor.html", {"mi_formulario": mi_formulario})


def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            for clave, valor in datos.items():
                setattr(profesor, clave, valor)
            profesor.save()
            return render(request, "formulario_profesor.html", {"mensaje": "Profesor editado correctamente"})
    else:
        mi_formulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 
                                                    'email': profesor.email, 'especialidad': profesor.especialidad})
    return render(request, "editar_profesor.html", {"mi_formulario": mi_formulario, "profesor": profesor})

def elimina_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    return render(request, "formulario_profesor.html", {"mensaje": "Profesor eliminado correctamente"})



def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = AlumnoFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Alumno.objects.create(**datos)
            return render(request, "formulario_alumno.html", {"mensaje": "Alumno creado correctamente"})
    else:
        mi_formulario = AlumnoFormulario()
    return render(request, "formulario_alumno.html", {"mi_formulario": mi_formulario})


def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = AlumnoFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            for clave, valor in datos.items():
                setattr(alumno, clave, valor)
            alumno.save()
            return render(request, "formulario_alumno.html", {"mensaje": "Alumno creado correctamente"})
    else:
        mi_formulario = AlumnoFormulario(initial={'nombre': alumno.nombre, 'apellido': alumno.apellido, 'email': alumno.email, 'fecha_nacimiento': alumno.fecha_nacimiento})
    return render(request, "editar_alumno.html", {"mi_formulario": mi_formulario, "alumno": alumno})

def elimina_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return render(request, "formulario_alumno.html", {"mensaje": "Alumno eliminado correctamente"})


def entregable_formulario(request):
    if request.method == "POST":
        mi_formulario = EntregableFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            Entregable.objects.create(**datos)
            return render(request, "formulario_entregable.html", {"mensaje": "Entregable creado correctamente"})
    else:
        mi_formulario = EntregableFormulario()
    return render(request, "formulario_entregable.html", {"mi_formulario": mi_formulario})


def editar_entregable(request, id):
    entregable = Entregable.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = EntregableFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            for clave, valor in datos.items():
                setattr(entregable, clave, valor)
            entregable.save()
            return render(request, "formulario_entregable.html", {"mensaje": "Entregable editado correctamente"}) 
    else:
        mi_formulario = EntregableFormulario(initial={'titulo': entregable.titulo, 'descripcion': entregable.descripcion, 'fecha_de_entrega': entregable.fecha_de_entrega, 'entregado': entregable.entregado})
    return render(request, "editar_entregable.html", {"mi_formulario": mi_formulario, "entregable": entregable})

def elimina_entregable(request, id):
    entregable = Entregable.objects.get(id=id)
    entregable.delete()
    return render(request, "formulario_entregable.html", {"mensaje": "Entregable eliminado correctamente"})  

def alumnos(request):
    alumnos_guardados = Alumno.objects.all()
    return render(request , "alumnos.html", {"alumnos": alumnos_guardados})


def profesores(request):
    profesores_guardados = Profesor.objects.all()
    return render(request , "profesores.html", {"profesores": profesores_guardados})


def entregables(request):
    entregables_guardados = Entregable.objects.all()
    return render(request , "entregables.html", {"entregables": entregables_guardados} )


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"url":avatares[0].imagen.url})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")


    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})




def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})




def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})

