from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tour

@login_required
def index(request):
    """ Vista para atender la petición de la url / """
    # Obteniendo los datos mediantes consultas
    tours = Tour.objects.all()

    return render(request, "tours/index.html", {"tours":tours})
