from urllib.parse import urlparse
from django.urls import path
from .views import *

urlpatterns = [
    path('auth',AuthUser.as_view()),
    path('branches',branchesApi.as_view()),
    path('responsables',ResponsablesApi.as_view()),
    path('responsable/<str:matricule>',ResponsableApi.as_view()),
    path('techniciens',TechniciensApi.as_view()),
    path('technicien/<str:matricule>',TechnicienApi.as_view()),
    path('ateliers',AteliersApi.as_view()),
    path('atelier/<str:code>',AtelierApi.as_view())
]

