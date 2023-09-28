from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import Alumno
from django.db.models import Q

def inicio(request):
    return render(request,'inicio.html')


#REGISTRO
def registrarse(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('')
        else:
            return render(request,'registrarse.html',{'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registrarse.html', {'form': form})

#LOGIN

def logear(request):
    if request.user.is_authenticated:
        return render(request, 'login.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/listado') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
            #return redirect('/login')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

# LISTADO
def listado(request): 
    alumno_list = Alumno.objects.all()
    context = {"alumno_list": alumno_list}
    return render(request, 'alumnos.html', context)

# INSERTAR
def insertaralumno(request):
    if request.method == 'POST':
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]
        email = request.POST["email"]
        dni = request.POST["dni"]
        
        alumno = Alumno.objects.create(nombres=nombres, apellidos=apellidos, email=email, dni=dni)
        
        return redirect('/listado')
    return render(request, 'alumnos.html')

# EDITAR
def editar(request, idAlumno):
    alumno = get_object_or_404(Alumno, idAlumno=idAlumno)

    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        dni = request.POST.get('dni')

        alumno.nombres = nombres
        alumno.apellidos = apellidos
        alumno.email = email
        alumno.dni = dni

        # Guardar los cambios en el alumno
        alumno.save()

        return redirect('/listado')
    
    return render(request, 'alumnos.html', {'alumno': alumno})

# ELIMINAR
def eliminar(request, idAlumno):
    alumno = Alumno.objects.get(idAlumno=idAlumno)
    alumno.delete()
    return redirect('/listado')
