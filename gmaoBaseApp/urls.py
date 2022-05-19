from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth',AuthUser.as_view()),
    path('branches',branchesApi.as_view()),
    path('responsables',ResponsablesApi.as_view()),
    path('responsable/<str:matricule>',ResponsableApi.as_view()),
    path('techniciens',TechniciensApi.as_view()),
    path('technicien/<str:matricule>',TechnicienApi.as_view()),
    path('ateliers',AteliersApi.as_view()),
    path('atelier/<int:code>',AtelierApi.as_view()),
    path('machines',MachinesApi.as_view()),
    path('machine/<str:code>',MachineApi.as_view()),
    path('categoriMachines',CathergorieMachinesApi.as_view()),
    path('sousTraitences',sousTraitencesApi.as_view()),
    path('sousTraitence/<str:code>',sousTraitenceApi.as_view()),
    path('InteventionCuratives',InterventionCurativesApi.as_view()),
    path('InterventionCurative/<str:code>',InterventionsCuratifApi.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

