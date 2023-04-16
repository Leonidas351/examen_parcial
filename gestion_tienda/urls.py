from django.urls import path
from . import views
app_name='gestion_tienda'
urlpatterns=[
    path('',views.index,name='index'),
    path('admin_console',views.admin_console,name='admin_console'),
    path('log_out',views.log_out,name='log_out'),
    path('delete_user/<str:ind>',views.delete_user,name='delete_user'),
    path('details_user/<str:ind>',views.details_user, name='details_user'),
    path('newProduct/<str:ind>', views.newProduct, name='newProduct'),
    path('delete_product/<str:ind>',views.delete_product, name='delete_product')
]