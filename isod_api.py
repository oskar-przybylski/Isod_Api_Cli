#made by Oskar Przybylski on 1.11.2024

import requests
from colorama import Fore, Style, init
import time

base_url = "http://isod.ee.pw.edu.pl/isod-portal/wapi"
params = {
    "q": "mynewsheaders",
    "username": " :D   ", #wstaw login z isoda: "imie.nazwisko"
    "apikey": " :D   ",   #wstaw klucz api: "XXXXXXXXXX"
    "from": "0",
    "to": "5",
}

start_time = time.perf_counter()
response = requests.get(base_url, params=params)
end_time = time.perf_counter()

request_duration = end_time - start_time

if response.status_code == 200:
    data = response.json()
else:
    print("Błąd: ", response.status_code)

init();
print("\n");
print("─" * 44,Style.BRIGHT+Fore.YELLOW+"ISOD"+Style.RESET_ALL,"─" * 50,)
for item in data["items"]:
    if(item["type"]!=1000):
        if(item["type"]==1002):
            print(Fore.RED+item["subject"]+Style.RESET_ALL,"by ",item["modifiedBy"])
            print("─" * 100)
        else:
            print(item["subject"],"by ",item["modifiedBy"])
            print("─" * 100)
print(Style.DIM+f"Czas odpowiedzi serwera: {request_duration:.2f} sekundy"+Style.RESET_ALL)

