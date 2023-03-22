from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    select_team = State()
    edit_team = State()


