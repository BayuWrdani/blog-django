from django.shortcuts import render
from django.http import HttpResponse
from artikel.models import (Artikel)

def homepage(request):
    daftar_artikel = Artikel.objects.all()

    search = request.GET.get('search')
    if search:
        daftar_artikel = daftar_artikel.filter(judul__icontains=search)

    context = dict(
        daftar_artikel=daftar_artikel
    )
    return render(request,'home.html', context)