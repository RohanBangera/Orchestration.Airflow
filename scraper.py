import json
import requests

def json_scraper(url, filename, bucket):
    print('started running')
    response= requests.request("GET",url)
    json_data = response.json()

    with open(filename, 'w', encoding = 'utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii = False, indent =4)

    print('stopped running')
json_scraper('https://www.predictit.org/api/marketdata/all/','predicit-market.json','pdata-mbfr')