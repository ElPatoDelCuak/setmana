from django.shortcuts import render, redirect
from django.http import Http404

def home(request):
    return render(request, "setmana/home.html")


def dia(request, day: int):
    if day <= 0:
        return redirect('home')

    dias = {
        1: 'dilluns',
        2: 'dimarts',
        3: 'dimecres',
        4: 'dijous',
        5: 'divendres',
        6: 'dissabte',
        7: 'diumenge',
    }

    try:
        nombre = dias[day]
    except KeyError:
        raise Http404('Dia no valid, introdueix un nombre entre 1 i 7, o 0 y negatius per tornar a la pàgina principal.')

    return render(request, 'setmana/dies.html', {'day': day, 'day_name': nombre , 'image_url': dias[day]})
