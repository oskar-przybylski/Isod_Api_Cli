import requests
import json
from colorama import Fore, Style,Back, init
import time

base_url = "http://isod.ee.pw.edu.pl/isod-portal/wapi"
params = {
    "q": "mynewsheaders",
    "username": "oskar.przybylski", #wstaw login z isoda: "imie.nazwisko"
    "apikey": "DBE9hffGMcme8QocZRzA0w",   #wstaw klucz api: "XXXXXXXXXX"
    "from": "0",
    "to": "5",
}

max_retries = 5
delay = 3

start_time = time.perf_counter()
for attempt in range(max_retries):
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        break
    except requests.exceptions.ConnectionError:
        print(f"Próba polaczenia z serwerem isod nr.{attempt + 1} nieudana. Ponawiam próbę za {delay} sekund...")
        time.sleep(delay)
    except requests.exceptions.HTTPError as err:
        print("Błąd HTTP:", err)
        break
else:
    print("Nie udało się nawiązać połączenia po maksymalnej liczbie prób.")
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

