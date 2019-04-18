from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'food/index.html')

def results(request, query_id):
    return HttpResponse("You're looking at the results of %s" % query_id)
