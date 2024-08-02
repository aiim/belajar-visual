import requests
import json

# Ganti dengan URL API Kobo Toolbox yang sesuai
url = 'https://mdc.pmi.or.id/api/v2/assets/aHqw7oYxjhUVbGBSyDuXTc/data/?format=json'
headers = {
    'Authorization': 'b1fd38dc369afc999d8f1eb0d060d00c4e71617a'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad HTTP status codes
    data = response.json()

    # Simpan data ke file JSON
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Data berhasil disimpan ke data.json")
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat mengambil data: {e}")
except json.JSONDecodeError as e:
    print(f"Terjadi kesalahan saat memproses data JSON: {e}")
except IOError as e:
    print(f"Terjadi kesalahan saat menulis file: {e}")
