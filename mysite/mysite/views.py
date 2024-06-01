from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("Main Page")

def error_404_view(request, exception):
    return HttpResponseNotFound("The page is not Found!@")