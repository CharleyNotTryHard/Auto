import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd10a24714e22bd2a37ac1ba1f253affe'
HEADER = {'Content-Type': 'application/json','trainer_token' : TOKEN}
body_confirmation = {"trainer_token": TOKEN}

body_registeation = {
    "trainer_token":TOKEN,
    "email": "@@@",
    "password": "@@@"
}
body_create = {
    "name": "generate",
    "photo_id": -1
}
response = requests.post(url = f'{URL}/trainers/reg', headers= HEADER, json = body_registeation)
print(response.text)

response_confirmation = requests.post(url= f'{URL}trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)

response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text)

message = response_create.json()['message']
print(message)