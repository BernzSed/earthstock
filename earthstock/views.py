from django.http import HttpResponse
from django.shortcuts import render
from earthstock.models import Stock, Quote

# these next two imports could be useful for generating a kmz, if needed
#from cStringIO import StringIO
#import zipfile



def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def earthstock(request):
	# template = loader.get_template('earthstock.html')
	# context = RequestContext(request)
	data = {'hello':'hello world!'}
	# return HttpResponse(template.render(context))
	return render(request, 'earthstock.html', data)
    

def stocks_kml(request):
    context = {
        'quotes': Quote.objects.select_related()
    }
    return render(request, 'stocks.kml', context, content_type='application/vnd.google-earth.kml+xml');
    #return render(request, 'stocks.kml', context);
    
