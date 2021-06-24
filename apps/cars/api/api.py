from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.cars.api.serializers import CarSerializer
from apps.cars.models import Car
from rest_framework import status

@api_view(['GET','POST'])
def car_api_view(request):

    if request.method == 'GET:':
        cars = Car.objects.all()
        cars_serializer = CarSerializer(cars,many = True)
        return Response(cars_serializer.data)

    elif request.method == 'POST':
        cars_serializer = CarSerializer(data = request.data)
        if cars_serializer.is_valid():
            cars_serializer.save()
            return Response(cars_serializer.data)
        return Response(cars_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def car_detail_api_view(request,pk=None):
    # queryset
    car = Car.objects.filter(id = pk).first()

    # validation
    if car:

        # retrieve
        if request.method == 'GET': 
            car_serializer = CarSerializer(car)
            return Response(car_serializer.data,status = status.HTTP_200_OK)
        
        # update
        elif request.method == 'PUT':
            car_serializer = CarSerializer(car,data = request.data)
            if car_serializer.is_valid():
                car_serializer.save()
                return Response(car_serializer.data,status = status.HTTP_200_OK)
            return Response(car_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        # delete
        elif request.method == 'DELETE':
            car.delete()
            return Response({'message':'CARRO Eliminado correctamente!'},status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado un CARRO con estos datos'},status = status.HTTP_400_BAD_REQUEST)