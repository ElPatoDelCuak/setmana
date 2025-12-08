from django.shortcuts import render

#Diccionari de personatges
personatges = {
    "Johnny_Silverhand": {
        "nom" : "Johnny Silverhand",
        "frase" : "I saw corps ... transform Night City into a machine fueled by people's crushed spirits, broken dreams and emptied pockets. Corps've long controlled our lives, taken lots... and now they're after our souls! ... I've declared war not 'cause capitalism's a thorn in my side or outta nostalgia for an America gone by. This war's a people's war against a system that's spiralled outta our control.",
        "img" : "/static/img/jhonny.png",
        "opcio" : "/P2_templates/Johnny_Silverhand/"
    },
    "John_Hammond": {
        "nom" : "John Hammond",
        "frase" : "Welcome to Jurassic Park!",
        "img" : "/static/img/john.png",
        "opcio" : "/P2_templates/John_Hammond/"
    },
    "Obi_Wan_Kenobi": {
        "nom" : "Obi-Wan Kenobi",
        "frase" : "Hello there",
        "img" : "/static/img/obi-wan.png",
        "opcio" : "/P2_templates/Obi_Wan_Kenobi/"
    },
    "Arthur_Morgan": {
        "nom" : "Arthur Morgan",
        "frase" : "We’re Thieves In A World That Don’t Want Us No More",
        "img" : "/static/img/arthur.png",
        "opcio" : "/P2_templates/Arthur_Morgan/"
    },
    "Lara_Croft" : {
        "nom" : "Lara Croft",
        "frase" : "When Life Flashes Before Us, We Find Something; Something That Keeps Us Going.",
        "img" : "/static/img/lara.png",
        "opcio" : "/P2_templates/Lara_Croft/"
    }
}

def home(request):
    return render(request, "P2_templates/home.html", {"personatges": personatges.values()})
    #Vista de personatges

#Vista de personatge específic
def personatge(request, personatge):
    if personatge in personatges:
        context = personatges[personatge]
        return render(request, "P2_templates/home.html", context)
    else:
        return render(request, "P2_templates/home.html", {"error": True}, status=404)
    #Vista d'error si el personatge no existeix al diccionari