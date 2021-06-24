from apps.cars.models import Car
from rest_framework import generics
from apps.cars.api.serializers import CarSerializer
from rest_framework.views import APIView
from apps.token import TokenHandler
from rest_framework.response import Response
from rest_framework import status

class CarListAPIView(TokenHandler,APIView):
    def get(self, request):
        payload,_ = self.get_payload(request)
        if not payload :
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(Car.objects.all().values(),status=status.HTTP_200_OK)

    def post(self, request):
        payload,user = self.get_payload(request)
        if not payload or not user.is_staff:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        car = Car.objects.create(**request.data)
        return Response({"id": car.id },status=status.HTTP_201_CREATED)

    def delete(self, request):
        payload,user = self.get_payload(request)
        if not payload or not user.is_staff:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        Car.objects.filter(id = request.data['id']).delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request):
        payload,user = self.get_payload(request)
        if not payload or not user.is_staff:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        car = Car.objects.filter(id = request.data['id'])    
        request.data.pop('id')
        if not car:
            return Response(status=status.HTTP_404_NOT_FOUND)
        car.update(**request.data)            
        return Response(status=status.HTTP_200_OK)

        

