import requests
import json

# Ganti dengan URL API Kobo Toolbox yang sesuai
url = 'https://mdc.pmi.or.id/api/v2/assets/aHqw7oYxjhUVbGBSyDuXTc/data/?format=json'
headers = {
    'Authorization': 'b1fd38dc369afc999d8f1eb0d060d00c4e71617a'
}

response = requests.get(url, headers=headers)
data = response.json()

# Simpan data ke file JSON
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
