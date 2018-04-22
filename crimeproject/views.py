from django.http import HttpResponse
from django.template import Context, Template, loader

def index(request):
    template = loader.get_template('stayfe.html')
    return HttpResponse(template.render())

def main(request):
    template = loader.get_template('stayfe.html')
    return HttpResponse(template.render())
    
def intro(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())

def content(request):
    template = loader.get_template('map.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contacts.html')
    return HttpResponse(template.render())

# def map(request):
#     template = loader.get_template('_map.html')
#     return HttpResponse(template.render())

