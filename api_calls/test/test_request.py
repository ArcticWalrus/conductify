import requests
import json

url = "https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs?query=hello&page=1&size=1"

payload = {}
headers = {
    'Authorization' : '51fal5fybpmqk0i2v1potkxoh1neqbu1'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.content)
print(data)
print(type(data))
print(data['songs'])
print(type(data['songs']))
for song in data['songs']:
    print(song['id'])
print(data['songs'])
if not data['songs']:
    print('No match found')




#json_data = json.dumps(response.json(), indent=4)

#print(json_data)

