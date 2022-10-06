from django.http import HttpResponse
from django.template import Context, Template, loader
from familiares.models import Familiar
from datetime import datetime
import random
from random import randrange

def crear_familiar(request, nombre, apellido,):
    familiar = Familiar(nombre = nombre, apellido = apellido, edad = random.randrange(1,99), fecha_carga = datetime.now(),)
    familiar.save()
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({'familiar': familiar})
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    familiares = Familiar.objects.all()
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares': familiares})
    return HttpResponse(template_renderizado)