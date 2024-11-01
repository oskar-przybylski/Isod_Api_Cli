import requests

base_url = "http://isod.ee.pw.edu.pl/isod-portal/wapi"
params = {
    "q": "mynewsheaders",
    "username": " :D ", #wstaw login z isoda: "imie.nazwisko"
    "apikey": " :D ",   #wstaw klucz api: "XXXXXXXXXX"
    "from": "0",
    "to": "5",
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
else:
    print("Błąd: ", response.status_code)

print("-" * 100)
for item in data["items"]:
    if(item["type"]!=1000):
        print(item["subject"]," by ",item["modifiedBy"])
        print("-" * 100)