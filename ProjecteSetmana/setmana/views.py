from django.shortcuts import render, redirect
from django.http import Http404

def home(request):
    return render(request, "setmana/home.html")


def dia(request, day: int):
    if day <= 0:
        return redirect('home')

    dias = {
        1: 'Dilluns',
        2: 'Dimarts',
        3: 'Dimecres',
        4: 'Dijous',
        5: 'Divendres',
        6: 'Dissabte',
        7: 'Diumenge',
    }

    img = {
        1: '/static/dilluns.jpg',
        2: '/static/dimarts.jpg',
        3: '/static/dimecres.jpg',
        4: '/static/dijous.jpg',
        5: '/static/divendres.jpg',
        6: '/static/dissabte.jpg',
        7: '/static/diumenge.jpg',
    }

    try:
        nombre = dias[day]
    except KeyError:
        raise Http404('Dia no valid, introdueix un nombre entre 1 i 7, o 0 y negatius per tornar a la pàgina principal.')

    return render(request, 'setmana/dies.html', {'day': day, 'day_name': nombre , 'image_url': img[day]})
