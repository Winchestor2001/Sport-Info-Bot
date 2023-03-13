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


