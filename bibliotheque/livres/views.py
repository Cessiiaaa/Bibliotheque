from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from .forms import SignUpForm, LivreForm
from .models import Livre

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_livres')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def liste_livres(request):
    query = request.GET.get('q', '')
    if query:
        posts = Livre.objects.filter(
            Q(titre__icontains=query) | Q(description__icontains=query)
        ).order_by('-date_de_publication')
    else:
        posts = Livre.objects.all().order_by('-date_de_publication')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'livres_etudiants/livres_list.html', {
        'page_obj': page_obj,
        'query': query
    })

@login_required
def livre_create(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            livre = form.save(commit=False)
            livre.proprietaire = request.user
            livre.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'livres_etudiants/livre_form.html', {'form': form, 'action': 'Créer'})

def livre_detail(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    return render(request, 'livres_etudiants/livre_detail.html', {'livre': livre})

@login_required
def livre_update(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.user != livre.proprietaire:
        raise PermissionDenied

    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm(instance=livre)
    return render(request, 'livres_etudiants/livre_form.html', {'form': form, 'action': 'Modifier'})

@login_required
def livre_delete(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.user != livre.proprietaire:
        raise PermissionDenied

    if request.method == 'POST':
        livre.delete()
        return redirect('liste_livres')
    return render(request, 'livres_etudiants/livre_confirm_delete.html', {'livre': livre})