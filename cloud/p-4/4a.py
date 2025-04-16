import requests 
import webbrowser
API_KEY=open("API_KEY").read().strip()
SEARCH_ENGINE_ID=open("SEARCH_ENGINE_ID").read().strip()
inp=input("enter something for searching:")
search_query=inp
url="https://www.googleapis.com/customsearch/v1"
params={
    'q':search_query,
    'key':API_KEY,
    'cx':SEARCH_ENGINE_ID
}
response=requests.get(url,params=params)
if response.status_code==200:
    results=response.json()
    if 'items' in results and len(results['items'])>0:
        first_link=results['items'][0]['link']
        print("successfully found:",first_link)
        webbrowser.open(first_link)
    else:
        print("no result found")

elif response.status_code==400:
    print("Bad request error(400):",response.json())
else:
    print(f"HTTP Error {response.status_code}:{response.text}")
                      
