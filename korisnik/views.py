from django.shortcuts import render

from .models import Korisnik
# Create your views here.

def korisnik_view(request):
    queryset = Korisnik.objects.order_by("id")

    context = {
        "obj_list": queryset
    }

    return render(request, "home.html", context)

