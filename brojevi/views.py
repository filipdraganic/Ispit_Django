from django.shortcuts import render

# Create your views here.
from brojevi.models import BrojeviForma, GrafForma, FilterForma
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
    prvoPolje = None
    drugoPolje = None
    listaImena = []
    if request.method == "POST":
        form = GrafForma(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            prvoPolje = form.cleaned_data.get("prvoPolje")
            drugoPolje = form.cleaned_data.get("drugoPolje")
            queryset1 = []
            queryset2 = []
            query = []
            if 'Korisnik' in prvoPolje:
                sviPrvi = list(Korisnik.objects.all())
            else:
                sviPrvi = list(Oglas.objects.all())

            if 'Korisnik' in drugoPolje:
                sviDrugi = list(Korisnik.objects.all())
            else:
                sviDrugi = list(Oglas.objects.all())

            for obj, obj2 in zip(sviPrvi, sviDrugi):
                queryset1.append(obj.getZeljenoPolje(prvoPolje))
                queryset2.append(obj2.getZeljenoPolje(drugoPolje))
                query += [{"x": obj.getZeljenoPolje(drugoPolje), "y": obj2.getZeljenoPolje(prvoPolje)}]
                listaImena.append(obj.ime)

            # print(queryset1)
            # print(queryset2)
            # print(query)
            slika = query
            # trace1 = go.Scatter(x=queryset1, y=queryset2, marker={'color': 'red', 'symbol': 104, 'size': "10"} ,mode='Lines', name='1st Trace')
            #
            # data = go.Data([trace1])
            # layout = go.Layout(title='Meine nesto', xaxis={'title':'x1'}, yaxis={'title':'x2'})
            # figure = go.Figure(data=data, layout=layout)
            # div = opy.plot(figure, auto_open=False, output_type='div')
            # slika = div
    return render(request, 'graf.html', {'form': form, 'slika': slika, 'listaImena': listaImena, 'prvoPolje': prvoPolje,
                                         'drugopolje': drugoPolje})


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


def filter_view(request, slug=None):
    form = FilterForma()
    context = {'render': False, 'form': form, 'slug': slug}
    lista = []

    if request.method == "POST":

        form = FilterForma(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            idOglasa = form.cleaned_data['id']
            ime = form.cleaned_data['ime']
            cena = form.cleaned_data['cena']
            brojPregleda = form.cleaned_data['brojPregleda']
            kategorija = form.cleaned_data['kategorija']
            preostaloVreme = form.cleaned_data['preostaloVreme']
            prodavacid = form.cleaned_data['prodavac_id']

            query = Oglas.objects.all()
            if idOglasa is not None:
                query = query.filter(id__contains=idOglasa)
            if ime is not '':
                query = query.filter(ime__contains=ime)
            if cena is not None:
                query = query.filter(cena__contains=cena)
            if brojPregleda is not None:
                query = query.filter(brojPregleda__contains=brojPregleda)
            if kategorija is not '':
                query = query.filter(kategorija__contains=kategorija)
            if preostaloVreme is not None:
                query = query.filter(preostaloVreme__contains=preostaloVreme)
            if prodavacid is not None:
                query = query.filter(prodavac__contains=prodavacid)

            for oglas in query:
                lista.append(oglas.toString())

            context['form'] = form

    if slug == 'korisnici':
        print("korisnici")
        context['render'] = True
        query = Korisnik.objects.all()
        for korisnik in query:
            lista.append(korisnik.toString())

    elif slug == 'oglasi':
        print("oglasi")
        context['render'] = True
        query = Oglas.objects.all()

        for oglas in query:
            lista.append(oglas.toString())

    elif slug == 'oglasiDetaljno':
        print("oglasi")
        context['render'] = True
        query = Oglas.objects.all()

    context['lista'] = lista

    return render(request, 'filter.html', context)
