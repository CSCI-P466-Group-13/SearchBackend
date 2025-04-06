from django.shortcuts import render, HttpResponse
from .models import car
from .models import property
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import propertySerializer
from .serializers import carSerializer



# Create your views here.
def index(response):
    return HttpResponse("Hello world!")

def search(request):
    houses = property.objects.all()
    return render(request, "search.html",{"houses": houses})

@api_view(['GET'])
def property_list(request):
    max_price = request.GET.get('price')
    min_beds = request.GET.get('beds')
    min_baths = request.GET.get('baths')
    min_sqft = request.GET.get('sqft')
    min_lot = request.GET.get('lot')
    year = request.GET.get("year")

    properties = property.objects.all()

    if max_price:
        properties = properties.filter(price__lte=max_price)
    if min_beds:
        properties = properties.filter(beds__gte=min_beds)
    if min_baths:
        properties = properties.filter(baths__gte=min_baths)
    if min_sqft:
        properties = properties.filter(square_feet__gte=min_sqft)
    if min_lot:
        properties = properties.filter(lot_size__gte=min_lot)
    if year:
        properties = properties.filter(year_built__gte=year)
    
    serializer = propertySerializer(properties, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def vehicle_list(request):
    price = request.GET.get('price')
    manufacturer = request.GET.get('make')
    model = request.GET.get('model')
    mileage = request.GET.get('mileage')
    max_year = request.GET.get('max_year')
    min_year = request.GET.get('min_year')
    
    cars = car.objects.all()

    if manufacturer:
        cars = cars.filter(manufacturer__icontains=manufacturer)
    if model:
        cars = cars.filter(model__icontains=model)
    if mileage:
        cars = cars.filter(mileage__lte=mileage)
    if max_year:
        cars = cars.filter(year__lte=max_year)
    if min_year:
        cars = cars.filter(year__gte=min_year)
    if price:
        cars = cars.filter(price__lte=price)

    serializer = carSerializer(cars, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def all_list(request):
    max_price = request.GET.get('price')
    min_beds = request.GET.get('beds')
    min_baths = request.GET.get('baths')
    min_sqft = request.GET.get('sqft')
    min_lot = request.GET.get('lot')
    year = request.GET.get("year")
    manufacturer = request.GET.get('make')
    model = request.GET.get('model')
    mileage = request.GET.get('mileage')
    max_year = request.GET.get('max_year')
    min_year = request.GET.get('min_year')

    properties = property.objects.all()
    cars = car.objects.all()

    if max_price:
        properties = properties.filter(price__lte=max_price)
    if min_beds or min_baths or min_sqft or min_lot or year:
        if min_beds:
            properties = properties.filter(beds__gte=min_beds)
        if min_baths:
            properties = properties.filter(baths__gte=min_baths)
        if min_sqft:
            properties = properties.filter(square_feet__gte=min_sqft)
        if min_lot:
            properties = properties.filter(lot_size__gte=min_lot)
        if year:
            properties = properties.filter(year_built__gte=year)
        properties_serializer = propertySerializer(properties, many=True)
        return Response(properties_serializer.data)
    elif manufacturer or model or mileage or max_year or min_year:
        if manufacturer:
            cars = cars.filter(manufacturer__icontains=manufacturer)
        if model:
            cars = cars.filter(model__icontains=model)
        if mileage:
            cars = cars.filter(mileage__lte=mileage)
        if max_year:
            cars = cars.filter(year__lte=max_year)
        if min_year:
            cars = cars.filter(year__gte=min_year)
        cars_serializer = carSerializer(cars,many=True)
        return Response(cars_serializer.data)
    else:
        properties_serializer = propertySerializer(properties, many=True)
        cars_serializer = carSerializer(cars,many=True)
        return Response(cars_serializer.data + properties_serializer.data)