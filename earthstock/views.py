from django.http import HttpResponse
from django.shortcuts import render
from earthstock.models import Stock, Quote
import requests

# these next two imports could be useful for generating a kmz, if needed
#from cStringIO import StringIO
#import zipfile



def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def earthstock(request):
	# template = loader.get_template('earthstock.html')
	# context = RequestContext(request)
	context = {'hello':'hello world!'}
	# return HttpResponse(template.render(context))
	return render(request, 'earthstock.html', context)
    

def stocks_kml(request):
    context = {
        'quotes': Quote.objects.select_related()
    }
    return render(request, 'stocks.kml', context, content_type='application/vnd.google-earth.kml+xml');
    #return render(request, 'stocks.kml', context);
    
def updatestocks(request):
	from earthstock.models import Stock, Quote
	from pprint import pprint
	from bs4 import BeautifulSoup
	print("updating stocks!")
	# get all stocks
	symbols = []
	all_stocks = Stock.objects.all()
	for stock in all_stocks:
		symbols.append(stock.symbol)
		# pprint(dir(stock))

	# pprint(symbols)
	yql = 'select symbol, LastTradePriceOnly, Change from yahoo.finance.quotes where symbol in ("' + '" , "'.join(symbols) + '")'
	# pprint(yql)
	# payload = {"q":yql
	# 					,"format":"xml"
	# 					,"env":"store%3A%2F%2Fdatatables.org"}
	# r = requests.get("http://query.yahooapis.com/v1/public/yql", params=payload)
	r = requests.get("http://query.yahooapis.com/v1/public/yql?format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&q="+yql)
	# print(r.status_code)
	# pprint(r.content)
	y=BeautifulSoup(r.content)
	# pprint(y)
	for quote in y.findAll('quote'):
		# print quote
		s = Stock.objects.get(symbol = quote["symbol"])
		# pprint(dir(s))
		# pprint(dir(quote))

		change = quote.findChild("change").text
		lastprice = quote.findChild("lasttradepriceonly").text
		# print lastprice
		# pprint(dir(change))
		# print change.text
		q = s.quote_set.first()  # one or none
		if q == None:
			q = Quote(stock=s)
		q.change = change
		q.price = lastprice
		q.save()
		print "success"
		# print quote["symbol"]
	# xmldoc = minidom.parse(r.content)
	# quotes = xmldoc.getElementsByTagName('quote')
	# print(len(quotes))
	# for quote in quotes:
	# 	print(quote.value)

	return render(request, 'updatestocks.html', {})
