import aiohttp

domain = "http://127.0.0.1:8000"


async def add_user_api(user_id: int, username: str):
    data = {"user_id": user_id, "username": username}
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{domain}/api/user/", data=data) as response:
            pass


async def get_users_api():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{domain}/api/user/") as response:
            return await response.json()


async def get_user_info_api(user_id):
    data = {'user_id': user_id}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{domain}/api/user_info/", data=data) as response:
            return await response.json()


async def update_liga_table_api(table):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{domain}/api/liga_table/", data=table) as response:
            pass


async def update_liga_player_api(player):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{domain}/api/liga_player/", data=player) as response:
            pass


async def update_top_team_api(tema):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{domain}/api/top_team/", data=tema) as response:
            pass


async def update_liga_calendar_api(tour):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{domain}/api/liga_calendar/", data=tour) as response:
            pass


async def get_liga_api():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{domain}/api/liga/") as response:
            return await response.json()


async def get_liga_table_api(liga):
    data = {'liga': liga}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{domain}/api/liga_table/", data=data) as response:
            return await response.json()


async def update_user_lang_api(user_id, lang):
    data = {'user': user_id, 'lang': lang}
    async with aiohttp.ClientSession() as session:
        async with session.put(f"{domain}/api/user_info/", data=data) as response:
            pass


async def get_teams_api():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{domain}/api/teams/") as response:
            return await response.json()


async def update_user_team_api(user_id, team):
    data = {'user': user_id, 'team': team}
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{domain}/api/user_info/", data=data) as response:
            pass


async def get_liga_tours_api(liga):
    data = {'liga': liga}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{domain}/api/tours/", data=data) as response:
            return await response.json()


async def get_liga_tour_api(liga, tour):
    data = {'liga': liga, 'tour': tour}
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{domain}/api/tour/", data=data) as response:
            return await response.json()


async def get_top_teams_api():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{domain}/api/top_team/") as response:
            return await response.json()


