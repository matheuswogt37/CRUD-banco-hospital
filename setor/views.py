from django.http import HttpResponse
from django.template import loader

def setor(request):
  template = loader.get_template('setorList.html')
  return HttpResponse(template.render())