from django.http import HttpResponse

def index(request):
    return HttpResponse("Testing rooms homepage")

def detail(request, room_id):
    return HttpResponse("Details for Room id: " + str(room_id))
