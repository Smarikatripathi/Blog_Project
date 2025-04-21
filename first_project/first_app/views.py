from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_obj = {
        'name': 'Smarika',
        'age': 22
    }
    # return render(request, 'first_app/index.html', context=my_dict)
    return render(request, template_name='first_app/index.html', context=my_obj)