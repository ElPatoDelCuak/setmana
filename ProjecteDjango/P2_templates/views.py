from django.shortcuts import render


personatges = {
    "Johnny_Silverhand": {
        "nom" : "Johnny Silverhand",
        "frase" : "Never fade away",
        "img" : "/static/img/jhonny.png",
        "opcio" : "/P2_templates/Johnny_Silverhand/"
    },
    "John_Hammond": {
        "nom" : "John Hammond",
        "frase" : "Welcome to Jurassic Park",
        "img" : "/static/img/john.png",
        "opcio" : "/P2_templates/John_Hammond/"
    },
    "Obi_Wan_Kenobi": {
        "nom" : "Obi-Wan Kenobi",
        "frase" : "May the Force be with you",
        "img" : "/static/img/obi-wan.png",
        "opcio" : "/P2_templates/Obi_Wan_Kenobi/"
    },
    "Arthur_Morgan": {
        "nom" : "Arthur Morgan",
        "frase" : "We are thieves in a world that don't want us no more",
        "img" : "/static/img/arthur.png",
        "opcio" : "/P2_templates/Arthur_Morgan/"
    },
    "Lara_Croft" : {
        "nom" : "Lara Croft",
        "frase" : "Adventure is out there",
        "img" : "/static/img/lara.png",
        "opcio" : "/P2_templates/Lara_Croft/"
    }
}

def home(request):
    return render(request, "P2_templates/home.html", {"personatges": personatges.values()})

def personatge(request, personatge):
    if personatge in personatges:
        persontage = personatges[personatge]
        return render(request, "P2_templates/personatge.html", persontage)
    else:
        return render(request, "P2_templates/error.html", status=404)