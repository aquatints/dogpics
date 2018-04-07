import requests

def query():
    url = "https://api.imgur.com/3/gallery/r/pics/time"
    header = "Authorization: Client-ID d88ae1ac1e85343"
    data = requests.get(url, header)
    text = data.text
    print(text)
    
query()