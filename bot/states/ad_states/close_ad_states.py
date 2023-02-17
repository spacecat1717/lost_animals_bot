from aiogram.dispatcher.filters.state import State, StatesGroup


class CloseAdState(StatesGroup):
    waiting_for_found_reason = State()

