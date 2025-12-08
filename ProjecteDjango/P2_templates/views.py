from django.shortcuts import render


personatges = {
    "Jhonny_Silverhand": {
        "Nom" : "Jhonny Silverhand",
        "Frase" : "Never fade away",
        "img" : "/static/jhonny.png"
    },
    "John_Hammond": {
        "Nom" : "John Hammond",
        "Frase" : "Welcome to Jurassic Park",
        "img" : "/static/hammond.png"
    },
    "Obi_Wan_Kenobi": {
        "Nom" : "Obi-Wan Kenobi",
        "Frase" : "May the Force be with you",
        "img" : "/static/obiwan.png"
    },
    "Arthur_Morgan": {
        "Nom" : "Arthur Morgan",
        "Frase" : "We are thieves in a world that don't want us no more",
        "img" : "/static/arthur.png"
    },
    "Lara_Croft" : {
        "Nom" : "Lara Croft",
        "Frase" : "Adventure is out there",
        "img" : "/static/lara.png"
    }
}

def home(request):
    """Home con mensaje."""
    var = "Hola Proba"
    return render(request, "P2_templates/home.html", {"var": var})