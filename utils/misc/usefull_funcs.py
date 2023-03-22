from fuzzywuzzy import fuzz
from aiogram.types import ReplyKeyboardMarkup
from datetime import datetime


async def get_text_ratio(data: list, text: str):
    teams = []
    for team in data:
        result = fuzz.partial_ratio(str(team['team']).lower(), text.lower())
        if result == 100:
            teams.append(team['team'])

    return teams


async def check_user_selected_liga(markup, selected: str):
    for kb in markup:
        for i in kb:
            if i['callback_data'] == selected:
                return i['text']


async def make_tour_context(data: list, tour_lang: str):
    context = f"🌀 <b>{data[0]['fields']['tour']} {tour_lang}</b>\n\n"
    for tour in data:
        date = datetime.strptime(
            datetime.strptime(tour['fields']['date'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M'),
            '%Y-%m-%d %H:%M')
        if date.hour == 00 and date.minute == 00:
            date = date.strftime('%Y-%m-%d')
        team = tour['fields']['team'].replace(" - ", f" {tour['fields']['score']} ")
        context += f"🕰 <b>{date}</b>\n" \
                   f"|{team}\n\n"

    return context


async def make_top_teams_context(data):
    context = ""
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    for team in data:
        context += f"{team['place']}) {team['team']} - {team['rate']}\n"
    context += f"\n🕰 {today}"
    return context


