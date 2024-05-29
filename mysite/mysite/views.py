from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("Main Page")

def error_404_view(reuqest, exception):
    return HttpResponseNotFound("The page is not found!#")