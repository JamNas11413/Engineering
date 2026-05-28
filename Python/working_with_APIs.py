import requests

base_url = ""

def get_data(endpoint):
    responce = requests.get(f"{base_url}/{endpoint}")
    
    if responce.status_code == 200:
        data = responce.json()
        return data
    else:
        print(f"Failed to retrive data {responce.status_code}")


info = get_data("")
print(info["name"])

