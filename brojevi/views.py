from django.shortcuts import render

# Create your views here.
from brojevi.models import BrojeviForma, GrafForma
from django.db import models
from oglas.models import Oglas
from oglas.models import Licitacija
from korisnik.models import Korisnik
import plotly.express as px
import plotly.offline as opy
import plotly.graph_objs as go

def graf_view(request):
    form = GrafForma()
    slika = None
    if request.method == "POST":
        form = GrafForma(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            prvoPolje = form.cleaned_data.get("prvoPolje")
            drugoPolje = form.cleaned_data.get("drugoPolje")
            queryset1 = []
            queryset2 = []
            query = []
            svi = list(Oglas.objects.order_by(prvoPolje))

            for oglas in svi:
                queryset1.append(oglas.getZeljenoPolje(prvoPolje))
                queryset2.append(oglas.getZeljenoPolje(drugoPolje))
                query += [{"x": oglas.getZeljenoPolje(drugoPolje), "y": oglas.getZeljenoPolje(prvoPolje)}]



            print(queryset1)
            print(queryset2)
            print(query)
            slika = query
            # trace1 = go.Scatter(x=queryset1, y=queryset2, marker={'color': 'red', 'symbol': 104, 'size': "10"} ,mode='Lines', name='1st Trace')
            #
            # data = go.Data([trace1])
            # layout = go.Layout(title='Meine nesto', xaxis={'title':'x1'}, yaxis={'title':'x2'})
            # figure = go.Figure(data=data, layout=layout)
            # div = opy.plot(figure, auto_open=False, output_type='div')
            # slika = div
    return render(request, 'graf.html', {'form': form, 'slika': slika})

def brojevi_view(request):
    form = BrojeviForma()
    slika = None
    queryset1 = None
    prvoPolje = None
    imenaOglasa = None
    if request.method == "POST":
        form = BrojeviForma(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            prvoPolje = form.cleaned_data.get("prvoPolje")
            queryset1 = []
            imenaOglasa = []
            if "Korisnik" in prvoPolje:
                print("Ima")
                svi = list(Korisnik.objects.all())
                for korisnik in svi:
                    queryset1.append(korisnik.getZeljenoPolje(prvoPolje))
                    imenaOglasa.append(korisnik.ime)

            else:
                svi = list(Oglas.objects.all())
                print("nema")
                for oglas in svi:
                    queryset1.append(oglas.getZeljenoPolje(prvoPolje))
                    imenaOglasa.append(oglas.ime)
            print(queryset1)
            slika = "nesto"
            print(imenaOglasa)

    return render(request, 'brojevi.html', {'form': form, 'query': queryset1, 'ime': prvoPolje,
                                            'imenaOglasa': imenaOglasa, "slike": slika})
