from django.shortcuts import render


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def earthstock(request):
	# template = loader.get_template('earthstock.html')
	# context = RequestContext(request)
	data = {'hello':'hello world!'}
	# return HttpResponse(template.render(context))
	return render(request, 'earthstock.html', data)