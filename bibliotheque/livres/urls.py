from django.contrib import admin
from django.urls import path
from .views import signup, liste_livres, livre_create, livre_detail, livre_update, livre_delete


urlpatterns = [
    path('', liste_livres, name='liste_livres'),
    path('livre/creer/', livre_create, name='livre_create'),
    path('livre/<int:pk>/', livre_detail, name='livre_detail'),
    path('livre/<int:pk>/modifier/', livre_update, name='livre_update'),
    path('livre/<int:pk>/supprimer/', livre_delete, name='livre_delete'),
    path('signup/', signup, name='signup'),
]

