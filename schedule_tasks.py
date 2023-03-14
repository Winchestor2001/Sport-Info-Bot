from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.misc.liga_parsers import laliga_table, laliga_player, top_teams, laliga_calendar

scheduler = AsyncIOScheduler(timezone='Asia/Tashkent')


def tasks():
    scheduler.add_job(laliga_calendar, trigger='interval', seconds=60)
    # scheduler.add_job(laliga_table, trigger='interval', seconds=5)
    # scheduler.add_job(laliga_player, trigger='interval', seconds=5)
    # scheduler.add_job(top_teams, trigger='interval', seconds=5)
    # pass
