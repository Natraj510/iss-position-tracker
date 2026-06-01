import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as err:
        print(f"Unexpected error occured:{err}")

url = "http://api.open-notify.org/iss-now.json"
data = fetch_data(url)

if data:
    print(data)
    print("Data extracted successfully")


