from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    path_to_bus = settings.BUS_STATION_CSV
    bus_stations = []
    with open(path_to_bus, 'r', encoding='utf-8') as file_:
        csv_file = csv.DictReader(file_)
        for row in csv_file:
            bus_stations.append(row)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, 5)
    page = paginator.get_page(page_number)
    print(page)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
