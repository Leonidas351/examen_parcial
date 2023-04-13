from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import userData,productData
# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        usuarioInfo = authenticate(request,username=nombreUsuario,password=contraUsuario)
        if usuarioInfo is not None:
            login(request,usuarioInfo)
            return HttpResponseRedirect(reverse('gestion_tienda:admin_console'))
        else:
            return HttpResponseRedirect(reverse('gestion_tienda:index'))
    return render(request,'login_page.html')


@login_required(login_url='http://127.0.0.1:8000')
def admin_console(request):
    if request.method == 'POST':
        users_first_name = request.POST.get('users_first_name')
        users_last_name = request.POST.get('users_last_name')
        users_email = request.POST.get('users_email')
        users_username = request.POST.get('users_username')
        users_password = request.POST.get('users_password')
        users_role = request.POST.get('users_role')
        users_cel_num = request.POST.get('users_cel_num')
        users_start_date = request.POST.get('users_start_date')
        usuarioNuevo = User.objects.create(
            username=users_username,
            email=users_email,
        )
        usuarioNuevo.set_password(users_password)
        usuarioNuevo.first_name = users_first_name
        usuarioNuevo.last_name = users_last_name
        usuarioNuevo.is_staff = True
        usuarioNuevo.save()

        userData.objects.create(
            user=usuarioNuevo,
            users_role = users_role,
            users_cel_num = users_cel_num
        )
        return HttpResponseRedirect(reverse('gestion_tareas:admin_console'))
    return render(request,'admin_console.html',{
        'all_users':User.objects.all().order_by('id')
    })

@login_required(login_url='http://127.0.0.1:8000')
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('gestion_tareas:index'))

def delete_user(request,ind):
    user_to_delete = User.objects.get(id=ind)
    userData.objects.get(user=user_to_delete).delete()
    user_to_delete.delete()
    return HttpResponseRedirect(reverse('gestion_tareas:admin_console'))

def details_user(request,ind):
    users_info=User.objects.get(id=ind)
    return render(request,'informacionUsuario.html',{'users_info':users_info,})