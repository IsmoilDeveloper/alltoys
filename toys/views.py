from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return HttpResponse('Welcome to Alltoys')
