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
        users_first_name = request.POST.get('users_first_name')
        users_password = request.POST.get('users_password')
        userInfo = authenticate(request,username=users_first_name,password=users_password)
        if userInfo is not None:
            login(request,userInfo)
            if userInfo.userdata.users_role == 'ADMINISTRADOR':
                return HttpResponseRedirect(reverse('gestion_tienda:admin_console'))
            else:
                return HttpResponseRedirect(reverse('gestion_tienda:details_user',kwargs={'ind':userInfo.id}))
                
        else:
            return HttpResponseRedirect(reverse('gestion_tienda:index'))
    return render(request,'login_page.html')

def details_user(request,ind):
    users_info=User.objects.get(id=ind)
    users_product = productData.objects.filter(registered_by=users_info).order_by('id')
    return render(request,'users_information.html',{
        'userInfo': users_info,
        'users_product': users_product
    })





#@login_required(login_url='http://127.0.0.1:8000')
def admin_console(request):
    if request.user.userdata.users_role == 'ADMINISTRADOR':
        if request.method == 'POST':
            users_first_name = request.POST.get('users_first_name')
            users_last_name = request.POST.get('users_last_name')
            users_email = request.POST.get('users_email')
            users_username = request.POST.get('users_username')
            users_password = request.POST.get('users_password')
            users_role = request.POST.get('users_role')
            users_cel_num = request.POST.get('users_cel_num')
            new_user = User.objects.create(
                username=users_username,
                email=users_email,
            )
            new_user.set_password(users_password)
            new_user.first_name = users_first_name
            new_user.last_name = users_last_name
            new_user.is_staff = True
            new_user.save()

            userData.objects.create(
                user=new_user,
                users_role = users_role,
                users_cel_num = users_cel_num
            )
            return HttpResponseRedirect(reverse('gestion_tienda:admin_console'))
        return render(request,'admin_console.html',{
            'all_users':User.objects.all().order_by('id')
        })
    else:
        return HttpResponseRedirect(reverse('gestion_tienda:details_user', kwargs={'ind':request.user.id}))
    

@login_required(login_url='http://127.0.0.1:8000')
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('gestion_tienda:index'))

def delete_user(request,ind):
    user_to_delete = User.objects.get(id=ind)
    #userData.objects.get(user=user_to_delete).delete()
    user_to_delete.delete()
    return HttpResponseRedirect(reverse('gestion_tienda:admin_console'))

def delete_product(request,ind):
    ind.product_name.delete()
    ind.product_code.delete()
    ind.price_bought.delete()
    ind.price_sold.delete()
    return HttpResponseRedirect(reverse('gestion_tienda:admin_console'))


def newProduct(request, ind):
    if request.method == 'POST':
        registered_by = User.objects.get(id=ind)
        product_name = request.POST.get('product_name')
        product_code = request.POST.get('product_code')
        price_bought = request.POST.get('price_bought')
        price_sold = request.POST.get('price_sold')
        productData.objects.create(
            product_name=product_name,
            product_code=product_code,
            price_bought=price_bought,
            price_sold=price_sold,
            registered_by=registered_by,
        )
        return HttpResponseRedirect(reverse('gestion_tienda:details_user', kwargs={'ind':ind}))