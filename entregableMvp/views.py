from django.http import HttpResponse
from django.template import Context, Template, loader
from familiares.models import Familiar

def crear_persona(request):
    return HttpResponse('hola')

def mi_template(request):
    template = loader.get_template('template.html')
    template_renderizado = template.render({'hola juancho'})
    return HttpResponse(template_renderizado)

def crear_familiar(request):
    return HttpResponse('')

def ver_familiares(request):
    
    familiares = Familiar.objects.all()
    
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares': familiares})
    
    return HttpResponse(template_renderizado)