from django.contrib import admin
from django.urls import path
from .views import signup, liste_livres, livre_create, livre_detail, livre_update, livre_delete


urlpatterns = [
    path('', liste_livres, name='liste_livres'),
    path('post/creer/', livre_create, name='creer_livre'),
    path('post/<int:pk>/', livre_detail, name='detail_livre'),
    path('post/<int:pk>/modifier/', livre_update, name='modifier_livre'),
    path('post/<int:pk>/supprimer/', livre_delete, name='supprimer_livre'),
    path('signup/', signup, name='signup'),
]

