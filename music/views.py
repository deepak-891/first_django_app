
# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>This is the music home pge</h1>")