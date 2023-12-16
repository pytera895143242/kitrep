from aiogram import types
from misc import dp, bot
from .sqlit import reg_user, info_members, cheak_black,status_access,update_status_access
from .callbak_data import reg_p
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1002102259287
reg_user(1,1)  # Запуск в БД


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    try:
        reg_user(message.chat.id, message.from_user.full_name)  # Регистрация в БД
    except:
        pass

    s = status_access(message.chat.id)
    if s == "1":
        await message.answer("Введите пароль!")

    else:
        if int(cheak_black(message.chat.id)) == 0:
            markup = types.InlineKeyboardMarkup()
            bat_b = types.InlineKeyboardButton(text='🏁START🏁', callback_data='go_7')
            markup.add(bat_b)

            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 50, reply_markup=markup)
