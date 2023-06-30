import requests
import json

# GET
# status='available'
# res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
#                     headers = {'accept': 'application/json'})
# print(res.status_code, 'запрос Get')
# print(res.json())
#

#POST
data_2 = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res2 = requests.post(f'https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
                      data = json.dumps(data_2))
print(res2.status_code, 'запрос Post')
print(res2.json())


#DELETE
res3 = requests.delete(f'https://petstore.swagger.io/v2/pet/9223372036854771554', headers = {'accept': 'application/json'})
print(res3.status_code, 'запрос DELETE')
print(res3.json())

#PUT

data = {
 "id": 9223372036854771475,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res4 = requests.put(f'https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
data = json.dumps(data))
print(res4.status_code, 'запрос PUT')
print(res4.json())

