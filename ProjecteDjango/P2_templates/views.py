from django.shortcuts import render, redirect
from django.http import Http404

def home(request):
    return render(request, "P2_templates/home.html")


def personatge(request, personatge):
    if personatge == "home":
        return redirect('home')

    personatges = {
        1: 'dilluns',
        2: 'dimarts',
        3: 'dimecres',
        4: 'dijous',
        5: 'divendres',
        6: 'dissabte',
        7: 'diumenge',
    }

    try:
        nom = personatges[personatge]
    except KeyError:
        raise Http404('Dia no valid, introdueix un nombre entre 1 i 7, o 0 y negatius per tornar a la pàgina principal.')

    return render(request, 'P2_templates/personatges.html', {'personatge': personatge, 'personatge_nom': nom , 'image_url': personatges[personatge]})
