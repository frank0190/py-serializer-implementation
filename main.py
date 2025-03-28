from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    parsed_data = JSONParser().parse(json)
    serializer = CarSerializer(data=parsed_data)

    if serializer.is_valid():
        car_instance = Car.objects.create(**serializer.validated_data)
        return car_instance
    else:
        raise ValueError("Invalid data provided to deserialize")
