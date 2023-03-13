import requests
from bs4 import BeautifulSoup
import lxml


async def laliga():
    url = "https://www.skysports.com/la-liga-table"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    tbody = soup.find('tbody')

    tr = tbody.find_all('tr')
    for t in tr:
        td = t.find_all('td')
        team, p, w, l, d, s = td[1], td[2], td[3], td[4], td[5], td[-2]
        print(team.text, p.text, w.text, l.text, d.text, s.text)
        print('*' * 50)

