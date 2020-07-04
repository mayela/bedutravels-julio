from django.shortcuts import render

def index(request):
    """ Vista para atender la petición de la url / """
    return render(request, "tours/index.html")