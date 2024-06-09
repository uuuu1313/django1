from datetime import date

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(('GET',))
def greeting(request):
    return Response("hello")

def sayHello():
    return "hello"

def get_today():
    return date.today()

def function_to_get_today():
    day = get_today()
    return day