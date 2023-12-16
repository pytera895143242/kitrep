import random

from aiogram import types
from misc import dp,bot
import asyncio
from .sqlit import update_status_access
from .admin import new_password1,new_password2,new_password3,new_password4,new_password5,new_password6,new_password7,new_password8,new_password9
from .admin import new_password10, new_password11, new_password12,new_password13,new_password14,new_password15,new_password16,new_password17,new_password18,new_password19

ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID = [ADMIN_ID_1,ADMIN_ID_2]
channel = -1001987012532
flag1 = 1 #НАСТРОЙКА РЕЖИМА ПОКАЗА FILE ID

@dp.message_handler(content_types=['text', 'photo', 'video_note', 'animation', 'document', 'video','file'])
async def all_message(message: types.Message):
    from .admin import passwd1,passwd2,passwd3,passwd4,passwd5,passwd6,passwd7,passwd8,passwd9
    from .admin import passwd10, passwd11, passwd12, passwd13, passwd14, passwd15, passwd16, passwd17, passwd18, passwd19

    if str(passwd1) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        await bot.send_message(chat_id=channel,text= f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass1""")
        update_status_access(message.chat.id)
        new_password1()

    elif str(passwd2) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password2()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass2""")

    elif str(passwd3) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password3()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass3""")

    elif str(passwd4) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password4()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass4""")

    elif str(passwd5) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password5()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass5""")

    elif str(passwd6) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password6()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass6""")

    elif str(passwd7) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password7()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass7""")

    elif str(passwd8) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password8()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass8""")

    elif str(passwd9) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password9()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass9""")


    elif str(passwd10) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password10()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass10""")


    elif str(passwd11) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass11""")
        update_status_access(message.chat.id)
        new_password11()

    elif str(passwd12) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password12()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass12""")

    elif str(passwd13) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password13()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass13""")

    elif str(passwd14) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password14()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass14""")

    elif str(passwd15) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password15()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass15""")

    elif str(passwd16) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password16()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass16""")

    elif str(passwd17) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password17()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass17""")

    elif str(passwd18) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password18()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass18""")

    elif str(passwd19) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)
        new_password19()
        await bot.send_message(chat_id=channel, text=f"""Пользователь: {message.from_user.first_name}
Пароль: {message.text}
Команда: pass19""")



    else:
        await message.answer('Неверный пароль')