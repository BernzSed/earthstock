import httplib2
import sys
from pprint import pprint

from apiclient import discovery


def main(argv):
  # Create an httplib2.Http object to handle our HTTP requests .
  http = httplib2.Http()

  # Construct the service object for the interacting with the Freebase Search.
  service = discovery.build('freebase', 'v1',  developerKey='AIzaSyCvBTWd3tg74-bwI16Xft8899gi_UovYtM', http=http)

  # print "Success! Now add code here."
  import json
  import urllib

  query = 'Huntington Bancshares Incorporated'
  service_url = 'https://www.googleapis.com/freebase/v1/search'
  api_key = 'AIzaSyCvBTWd3tg74-bwI16Xft8899gi_UovYtM'
  # topic_id
  params = {
  'query': query,
  'key': api_key
  }
  url = service_url + '?' + urllib.urlencode(params)
  response = json.loads(urllib.urlopen(url).read())
  # pprint(response)
  topic_id = response['result'][0]['mid']
  params = {
    'key': api_key,
    'filter': '/organization/organization/headquarters'
  }
  service_url = 'https://www.googleapis.com/freebase/v1/topic'
  url = service_url + topic_id + '?' + urllib.urlencode(params)
  topic = json.loads(urllib.urlopen(url).read())
  # pprint(topic)
  # topic_id = '/m/0d6lp'
  # params = {
  #   'key': api_key,
  #   'filter': 'suggest'
  # }
  # url = service_url + topic_id + '?' + urllib.urlencode(params)
  # topic = json.loads(urllib.urlopen(url).read())
  # pprint(topic)
  for property in topic['property']:
    print property + ':'
    for value in topic['property'][property]['values']:
      print ' - ' + value['text']
  # for result in response['result']:
  #   print result['name'] + ' (' + str(result['score']) + ')'


# For more information on the Freebase Search you can visit:
#
#   

#
# For more information on the Freebase Search Python library surface you
# can visit:
#
#   https://developers.google.com/resources/api-libraries/documentation/freebase/v1/python/latest/
#
# For information on the Python Client Library visit:
#
#   https://developers.google.com/api-client-library/python/start/get_started
if __name__ == '__main__':
  main(sys.argv)
