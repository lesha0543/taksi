import requests
import json
import time


url = "https://fleet-api.taxi.yandex.net/v1/parks/orders/list"
url_car = "https://fleet-api.taxi.yandex.net/v1/parks/cars/list"
url_driver = "https://fleet-api.taxi.yandex.net/v1/parks/driver-profiles/list"
id_car = ''
id_driver = []
headers = {
    "X-Client-ID": "taxi/park/bd0c5ec2afa44586978dab26e587c68b",
    "X-API-Key": "DtqbZWdlpccYYOMbuNNJmuxCxHbBOPiHKXhTZiWn",
}

headers_driver = {
    "X-Client-ID": "taxi/park/bd0c5ec2afa44586978dab26e587c68b",
    "X-API-Key": "DtqbZWdlpccYYOMbuNNJmuxCxHbBOPiHKXhTZiWn",
    "Accept-Language":"en",
}

data = {
  "limit": 1,
  "query": {
    "park": {
      "car": {
        "id": '007944d8ef9d0855389efed80e43e476'
      },
      "driver_profile": {
        "id": '64bb0c9e4c9e6131ee8d10335f6e07ef'
      },
      "id": 'bd0c5ec2afa44586978dab26e587c68b',
       "order":{
        "booked_at": {
          "from": "2022-10-10T14:17:38.895+0000",
          "to": "2022-12-23T22:00:00.895+0000",
        },
        "statuses": [
          "complete"
        ],

      }
    }
  }
}

data_car ={
    "query": {
        "park": {
            "id": "bd0c5ec2afa44586978dab26e587c68b"
        }
    }
}

data_driver ={
    "fields": {
        "driver_profile": [
            "first_name",
            "last_name",
            "id"
    ]
     },
        "query": {
        "park": {
            "id": "bd0c5ec2afa44586978dab26e587c68b"
        }

    }
 }

def responce(url, headers, data):
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

response_car = responce(url_car,headers,data_car)
response_driver = responce(url_driver,headers_driver,data_driver)

for keys in response_car['cars'][0].items():
    if keys[0] == "id":
        id_car = keys[1]

for keys in response_driver['driver_profiles']:
    for key in keys['driver_profile'].values():
        id_driver.append(key)

print(f'id авто:{id_car}')
print(f'id водителя:{id_driver}')
while True:
    print(responce(url,headers,data))
    time.sleep(1)
