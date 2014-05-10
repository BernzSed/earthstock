import csv
import json
import urllib
from pprint import pprint

if __name__ == '__main__':
  api_key = 'AIzaSyCvBTWd3tg74-bwI16Xft8899gi_UovYtM'

  # Dict keys
  # "Symbol","Name","LastSale","MarketCap","ADR TSO","IPOyear","Sector","industry","Summary Quote"
  # listOfIndustries = {}
  data = []
  f = csv.DictReader(open("companylist.csv"))
  for row in f:
    query = row["Name"]
    service_url = 'https://www.googleapis.com/freebase/v1/search'
    # topic_id
    params = {
    'query': query,
    'key': api_key
    }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())
    pprint(response)
    if(len(response['result']) == 0):
      continue
    topic_id = response['result'][0]['mid']
    params = {
      'key': api_key,
      'filter': '/organization/organization/headquarters'
    }
    service_url = 'https://www.googleapis.com/freebase/v1/topic'
    url = service_url + topic_id + '?' + urllib.urlencode(params)
    topic = json.loads(urllib.urlopen(url).read())
    pprint(topic)
    if not 'property' in topic.keys():
      data.append('')
    for property in topic['property']:
      value = ''
      print property + ':'
      for value in topic['property'][property]['values']:
        if 'text' in value.keys():
          print ' - ' + value['text']
      data.append(value)
  open("data.txt", "a").write("\n".join(data))
    # pprint(row)
  #   if not row["industry"] in listOfIndustries.keys():
  #     listOfIndustries[row["industry"]] = 1
  #   else:
  #     listOfIndustries[row["industry"]] += 1
  # pprint(listOfIndustries)
    # print(row["Name"])
  # with open('companylist.csv', mode='r') as infile:
  #   reader = csv.reader(infile)
  #   mydict = dict((rows[0],rows[1]) for rows in reader)
  # pprint(mydict)