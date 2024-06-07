# from django.http import HttpResponse
# from django.template import loader

# def setor(request):
#   template = loader.get_template('setorList.html')
#   return HttpResponse(template.render())


from django.http import HttpResponse
from .models import Setor

def setor(request):
  setor = Setor.objects.all()[:5]
  output = '<br>'.join([s.nome for s in setor])
  return HttpResponse(output)