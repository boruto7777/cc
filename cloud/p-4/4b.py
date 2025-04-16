import requests
API_KEY=open("API_KEY").read()
SEARCH_ENGINE_ID=open("SEARCH_ENGINE_ID").read()
search_query="cat"
url="https://www.googleapis.com/customsearch/v1"

params={
    'q':search_query,
    'key':API_KEY,
    'cx':SEARCH_ENGINE_ID
    }

response=requests.get(url,params=params)
results=response.json()['items']
for item in results:
    print(item['link'])