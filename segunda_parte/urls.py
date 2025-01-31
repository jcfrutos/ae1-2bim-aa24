from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='platotipico'),
    path('<int:platotipico_id>', views.detalle, name='platotipico_detalle'),
    path('create', views.formulario, name='platotipico_formulario'),
]