''' CREATED BY BOYD BIGDATA RPG -- DATA SCIENTIST
    FUNCTION USE FOR CONNECT TO ES USING PYTHON
    FINAL RESULT RETURN DATAFRAME IN FORM OF PANDAS
'''

from elasticsearch import Elasticsearch
import requests

def connectES(severname, port):
  ''' HOW TO USE
  Default
  severname = 'localhost'
  port = 9200
  '''

  ''' PART CONNECTION TO ES '''

  res = requests.get('http://localhost:9200')
  print('\n')
  print('=================== Check Get Request is From ES ===================')
  print(res)
  print('\n')

  es = Elasticsearch([{'host': severname, 'port': port}])
  return es




if __name__ == "__main__":
    connectES("localhost", 9200)