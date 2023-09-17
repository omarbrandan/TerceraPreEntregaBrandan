from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
#    path('athletes/', athletes, name='Athletes'),
#    path('competitions/', competitions, name='Competitions'),
#    path('store/', store, name='Store'),
#    path('athletes-formulario/', athletes_formulario, name='AthletesFormulario'),
#    path('competitions-formulario/', competitions_formulario, name='CompetitionsFormulario'),
#    path('store-formulario/', store_formulario, name='StoreFormulario'),
    path('busqueda-apellido/', busqueda_apellido, name='BusquedaApellido'),
    path('buscar/', buscar, name='Buscar'),
#    path('lista-athletes/', lista_athletes, name='ListaAthletes'),
#    path('lista-competitions/', lista_competitions, name='ListaCompetitions'),
#    path('lista-store/', lista_store, name='ListaStore'),
#    path('crea-athletes/', crea_athletes, name='CreaAthletes'),
#    path('crea-competitions/', crea_competitions, name='CreaCompetitions'),
#    path('crea-store/', crea_store, name='CreaStore'),
#    path('elimina-athletes/<int:id>', elimina_athletes, name='EliminaAthletes'),
#    path('elimina-competitions/<int:id>', elimina_competitions, name='EliminaCompetitions'),
#    path('elimina-store/<int:id>', elimina_store, name='EliminaStore'),
#    path('editar-athletes/<int:id>', editar_athletes, name='EditarAthletes'),
#    path('editar-competitions/<int:id>', editar_competitions, name='EditarCompetitions'),
#    path('editar-store/<int:id>', editar_store, name='EditarStore'),
    path('lista-athletes/', AthleteList.as_view(), name='ListaAthletes'),
    path('detalle-athletes/<pk>', AthleteDetail.as_view(), name='DetalleAthletes'),
    path('crea-athletes/', AthleteCreate.as_view(), name='CreaAthletes'),
    path('actualiza-athletes/<pk>', AthleteUpdate.as_view(), name='ActualizaAthletes'),
    path('elimina-athletes/<pk>', AthleteDelete.as_view(), name='EliminaAthletes'),
    path('lista-competitions/', CompetitionsList.as_view(), name='ListaCompetitions'),
    path('detalle-competitions/<pk>', CompetitionsDetail.as_view(), name='DetalleCompetitions'),
    path('crea-competitions/', CompetitionsCreate.as_view(), name='CreaCompetitions'),
    path('actualiza-competitions/<pk>', CompetitionsUpdate.as_view(), name='ActualizaCompetitions'),
    path('elimina-competitions/<pk>', CompetitionsDelete.as_view(), name='EliminaCompetitions'),
    path('lista-store/', StoreList.as_view(), name='ListaStore'),
    path('detalle-store/<pk>', StoreDetail.as_view(), name='DetalleStore'),
    path('crea-store/', StoreCreate.as_view(), name='CreaStore'),
    path('actualiza-store/<pk>', StoreUpdate.as_view(), name='ActualizaStore'),
    path('elimina-store/<pk>', StoreDelete.as_view(), name='EliminaStore'),
    path('login/', login_view, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name='Logout'),
    path('editar-perfil/', editar_perfil, name='EditarPerfil'),
    path('agregar-avatar/', agregar_avatar, name='AgregarAvatar'),
    path('about/', about, name='About'),
]