import json
import requests 
from requests_aws4auth import AWS4Auth

aws_access_key_id = '<Your_aws_access_key_id>'
aws_secret_access_key = '<Your_aws_secret_access_key>'
aws_session_token = '<Your_aws_session_token>'
endpoint = '<elasticSearch_endpoint>'
# Below code will be used while sending a request  
headers = { "Content-Type": "application/json" }
awsauth=AWS4Auth(aws_access_key_id,aws_secret_access_key, '<your_region>', 'es',session_token=aws_session_token)
# <your_region> is the region where you created es domain and took endpoint


# main function of your lambda
def es_search_main(event,context=None):
  UserData = getData()
  # The below condition is used to check whether data found or not
  if(len(UserData['hits']['hits'])==0):
       print("No userData Found")  
  else:
       for hit in UserData['hits']['hits']: #loop the data
            print("User Data\n",hit)
            # use hit['_source']['<required_filedname>'] to retreive the required feild data from your lambda
            print("User Name-->",hit['_source']['name']) 
          
          
# getData() will return the elasticSearch result
def getData():          
    index = "<your_table_index_name>"
    query = {
        "query":{
                    "match_all": {
                      }
        },
         "size": 10000    
    }
    url = endpoint + '/' + index + '/_search'
    result = json.loads(requests.get(url, headers=headers, data=json.dumps(query)).text)   
    return result