import requests
from bs4 import BeautifulSoup
import lxml
from datetime import datetime
from time import sleep

from api.backend_api import update_liga_table_api, update_liga_player_api, update_top_team_api, update_liga_calendar_api


async def laliga_table():
    url = "https://www.skysports.com/la-liga-table"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    tbody = soup.find('tbody')
    tr = tbody.find_all('tr')
    for t in tr:
        td = t.find_all('td')
        place, team, p, w, l, d, s = td[0], td[1], td[2], td[3], td[4], td[5], td[-2]
        await update_liga_table_api(
            {
                'liga': 'laliga',
                'place': int(place.text.strip()),
                'team': team.text.strip(),
                'games': int(p.text.strip()),
                'win': int(w.text.strip()),
                'lose': int(l.text.strip()),
                'goals': int(d.text.strip()),
                'score': int(s.text.strip()),
            }
        )


async def laliga_player():
    url = "https://www.sports.ru/la-liga/bombardiers/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    tbody = soup.find('tbody')
    tr = tbody.find_all('tr')
    for t in tr:
        td = t.find_all('td')
        place, player, team, m, g = td[0], td[1], td[2], td[3], td[4]
        await update_liga_player_api(
            {
                'liga': 'laliga',
                'place': int(place.text.strip()),
                'team': team.text.strip(),
                'player': player.text.strip(),
                'games': int(m.text.strip()),
                'goals': int(g.text.strip()),
            }
        )


async def top_teams():
    url = "https://one-versus-one.com/en/teams/best-football-teams"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    ranking_list = soup.find('div', attrs={'class': 'ranking-section__list'})

    places = ranking_list.find_all('div', attrs={'class': 'ranking-section__list-item-rank'})
    teams = ranking_list.find_all('div', attrs={'class': 'ranking-section__list-item-info'})
    indexes = ranking_list.find_all('div', attrs={'class': 'ranking-section__list-item-index'})

    counter = 0
    for place, team, index in zip(places, teams, indexes):
        if counter == 20:
            break
        await update_top_team_api(
            {
                'place': int(place.text.strip().replace('#', '')),
                'team': team.text.strip(),
                'rate': int(index.text.strip()),
            }
        )
        counter += 1


async def laliga_calendar():
    months = [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]

    for m in months:
        url = f"https://www.sports.ru/la-liga/calendar/?s=303926&m={m}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        tbody = soup.find_all('tbody')
        tours = soup.find_all('h3', attrs={"class": 'titleH3 bordered mB10'})

        for tb, t in zip(tbody, tours):
            dates = tb.find_all('td', attrs={'class': 'name-td alLeft'})
            owners = tb.find_all('td', attrs={'class': 'owner-td'})
            scores = tb.find_all('td', attrs={'class': 'score-td'})
            guests = tb.find_all('td', attrs={'class': 'guests-td'})
            for date, owner, score, guest in zip(dates, owners, scores, guests):
                team = owner.text.strip() + ' - ' + guest.text.strip()

                try:
                    date = datetime.strptime(str(date.text.strip().replace('|', ' ')), '%d.%m.%Y %H:%M')
                except ValueError:
                    date = datetime.strptime(str(date.text.strip().replace('|', ' ')), '%d.%m.%Y')

                tour = t.text.strip().replace(' тур', '')
                await update_liga_calendar_api(
                    {
                        'liga': 'laliga',
                        'tour': int(tour),
                        'team': team,
                        'score': score.text.strip(),
                        'date': date,
                    }
                )
        response.close()
        sleep(.5)






