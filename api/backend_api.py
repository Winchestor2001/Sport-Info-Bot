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


