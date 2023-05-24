import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import asyncio
import time

all_data = []

async def main():
    ua = UserAgent()
    headers = {
        'user-agent': ua.random
    }
    url = 'https://free-proxy-list.net/'
    print(url)
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    line = soup.find('table', class_='table table-striped table-bordered').find('tbody').find_all('tr')
    for tr in line:
        td = tr.find_all('td')
        ip = td[0].text.strip()
        port = td[1].text.strip()

        all_data.append({'proxy':ip+':'+port,
                         })
        print(len(all_data))

    with open('proxy_list.json', 'a', encoding='utf-8') as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    asyncio.run(main())
    time.sleep(10)