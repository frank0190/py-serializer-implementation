import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    car_data = JSONParser().parse(stream)
    serializer = CarSerializer(data=car_data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
