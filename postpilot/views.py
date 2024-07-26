from django.http import HttpResponse

def testserver(request):
    return HttpResponse("Server is running")