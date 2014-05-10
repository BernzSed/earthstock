from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def earthstock(request):
	template = loader.get_template('earthstock.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))