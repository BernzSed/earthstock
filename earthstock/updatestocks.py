from earthstock.models import Stock, Quote
from pprint import pprint

print("updating stocks!")
# get all stocks
all_stocks = Stock.objects.all()
for stock in all_stocks:
	pprint(stock)